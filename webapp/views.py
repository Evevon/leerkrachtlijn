from django import forms
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User
from django.core.mail import send_mail
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.urls import reverse
import operator
from .models import *


class NoteForm(forms.Form):
    cat_a_note = forms.CharField(widget=forms.Textarea(attrs={"rows":8, "cols":80}), required=False)
    cat_b_note = forms.CharField(widget=forms.Textarea(attrs={"rows":8, "cols":80}), required=False)
    cat_c_note = forms.CharField(widget=forms.Textarea(attrs={"rows":8, "cols":80}), required=False)
    cat_d_note = forms.CharField(widget=forms.Textarea(attrs={"rows":8, "cols":80}), required=False)
    cat_e_note = forms.CharField(widget=forms.Textarea(attrs={"rows":8, "cols":80}), required=False)
    cat_f_note = forms.CharField(widget=forms.Textarea(attrs={"rows":8, "cols":80}), required=False)
    cat_g_note = forms.CharField(widget=forms.Textarea(attrs={"rows":8, "cols":80}), required=False)



class UserForm(forms.Form):
    user_email = forms.EmailField(required=False)
    answer_q1 = forms.CharField(widget=forms.Textarea(attrs={"rows":8, "cols":80}), required=False)
    answer_q2 = forms.CharField(widget=forms.Textarea(attrs={"rows":8, "cols":80}), required=False)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("user_email")
        if User.objects.filter(email=email).exists():
            self.add_error("user_email", "Dit email adres wordt al door een account gebruikt.")


class NewStudentForm(forms.Form):
    studentnaam = forms.CharField()
    studentId = forms.CharField()
    email = forms.EmailField()

    def clean(self):
        cleaned_data = super().clean()
        studentname = cleaned_data.get("studentnaam")
        email = cleaned_data.get("email")
        student_id = cleaned_data.get("studentId")
        if User.objects.filter(username=studentname).exists():
            self.add_error("studentnaam", "Er bestaat al een account met deze naam.")
        if User.objects.filter(email=email).exists():
            self.add_error("email", "Dit email adres wordt al door een account gebruikt.")
        if User_Profile.objects.filter(student_id=student_id):
            self.add_error("studentId", "Er bestaat al een student met dit studentenId.")


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    studentId = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean(self):
        cleaned_data = super().clean()
        studentname = cleaned_data.get("studentnaam")
        email = cleaned_data.get("email")
        student_id = cleaned_data.get("studentId")
        if User.objects.filter(username=studentname).exists():
            self.add_error("studentnaam", "Er bestaat al een account met deze naam.")
        if User.objects.filter(email=email).exists():
            self.add_error("email", "Dit email adres wordt al door een account gebruikt.")
        if User_Profile.objects.filter(student_id=student_id):
            self.add_error("studentId", "Er bestaat al een student met dit studentenId.")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        cleanedstudentid = self.cleaned_data["studentId"]
        user.save()
        user.user_profile.student_id = cleanedstudentid
        user.is_active = False
        user.save()
        user.user_profile.save()
        return user


class NewTeacherForm(forms.Form):
    docentnaam = forms.CharField()
    email = forms.EmailField()

    def clean(self):
        cleaned_data = super().clean()
        teachername = cleaned_data.get("docentnaam")
        email = cleaned_data.get("email")
        if User.objects.filter(username=teachername).exists():
            self.add_error("docentnaam", "Er bestaat al een account met deze naam.")
        if User.objects.filter(email=email).exists():
            self.add_error("email", "Dit email adres wordt al door een account gebruikt.")


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            context = {
                'form' : SignUpForm(),
                'registered' : True,
            }
            return render(request, 'webapp/register.html', context)
    else:
        form = SignUpForm()
    context = {
        'form' : form,
    }
    return render(request, 'webapp/register.html', context)

@login_required
def change_password(request):
    if request.method == 'POST':
        if request.POST['form'] == "passwordform":
            passwordform = PasswordChangeForm(request.user, request.POST)
            if passwordform.is_valid():
                user = passwordform.save()
                update_session_auth_hash(request, user)  # Important!
                return render(request, 'webapp/change_password.html', {
                    'password_form': PasswordChangeForm(request.user),
                    'user_form' : UserForm(),
                    'password_changed' : True,
                })
            else:
                messages.error(request, 'Er is iets mis gegaan tijdens het wijzigen van jouw wachtwoord. Los de volgende fouten op.')
                userform = UserForm()
        elif request.POST['form'] == "emailform":
            userform = UserForm(request.POST)
            if userform.is_valid():
                request.user.email = userform.cleaned_data['user_email']
                request.user.save()
                return HttpResponseRedirect(reverse('change_password'))
            else:
                passwordform = PasswordChangeForm(request.user)
    else:
        passwordform = PasswordChangeForm(request.user)
        userform = UserForm()
    return render(request, 'webapp/change_password.html', {
        'password_form': passwordform,
        'user_form' : userform,
    })


@login_required
def update_active(request):
    if request.user.is_superuser:
        updated_user = User.objects.get(pk=int(request.POST['user_id']))
        if request.POST['form'] == "Zet op inactief":
            updated_user.is_active = False
        else:
            updated_user.is_active = True
        updated_user.save()
    return HttpResponseRedirect(reverse('manage_accounts'))

@login_required
def index(request):
    context = {}
    return render(request, 'webapp/index.html', context)


@login_required
def profile(request):
    if has_group(request.user, "Leerling"):
        user_ps_profile = request.user.user_profile.primary_skills_profile
        user_bpb_profile = request.user.user_profile.broad_professional_basis_profile
        user_pi_profile = request.user.user_profile.professional_identity_profile

        ps_categories, _, ps_subsubcategories = get_subsubcategories(1)
        bpb_categories, _, bpb_subsubcategories = get_subsubcategories(2)
        ps_profile_data = get_profile_data(user_ps_profile, ps_subsubcategories)
        bpb_profile_data = get_profile_data(user_bpb_profile, bpb_subsubcategories)
        context = {
            'ps_categories' : ps_categories,
            'bpb_categories' : bpb_categories,
            'ps_profile' : ps_profile_data,
            'bpb_profile' : bpb_profile_data,
            'pi_profile' : user_pi_profile,
        }
        return render(request, 'webapp/profile.html', context)
    else:
        raise Http404("Deze webpagina bestaat niet!")


@login_required
def profile_settings(request):
    if has_group(request.user, "Leerling"):
        all_teachers = User.objects.filter(groups__name='Docent', is_active=True)
        user_form = UserForm()
        context = {
            'user_form' : user_form,
            'all_teachers' : all_teachers,
        }
        return render(request, 'webapp/profile_settings.html', context)


@login_required
def update_email(request):
    if has_group(request.user, "Leerling"):
        form = UserForm(request.POST)
        if form.is_valid():
            request.user.email = form.cleaned_data['user_email']
            request.user.save()
            return HttpResponseRedirect(reverse('profile'))
    else:
        raise Http404("Deze webpagina bestaat niet!")


@login_required
def share_profile(request):
    if has_group(request.user, "Leerling"):
        current_user_sharelist = request.user.user_profile.profile_shared_list
        teacher = User.objects.get(id=int(request.POST['teacherId']))
        if request.POST['share'] == 'true':
            current_user_sharelist.add(teacher)
        elif request.POST['share'] == 'false':
            current_user_sharelist.remove(teacher)
        else:
            print('error, request.POST["share"] has invalid value.')
        return HttpResponseRedirect(reverse('profile_settings'))
    else:
        raise Http404("Deze webpagina bestaat niet!")


@login_required
def update_ps_profile(request):
    if has_group(request.user, "Leerling"):
        profile = request.user.user_profile.primary_skills_profile
        category_mapping = {'1':'A', '2':'B', '3':'C'}
        level = "level_{}_{}_{}".format(
          category_mapping[request.POST['category']],
          request.POST['subcategory'],
          request.POST['subsubcategory'])

        setattr(profile, level, request.POST['level'])
        profile.save()

        return HttpResponseRedirect("{}#categorie-1-{}-{}-{}".format(
                reverse('theory'),
                request.POST['category'],
                request.POST['subcategory'],
                request.POST['subsubcategory']))
    else:
        raise Http404("Deze webpagina bestaat niet!")


@login_required
def update_bpb_profile(request):
    if has_group(request.user, "Leerling"):
        profile = request.user.user_profile.broad_professional_basis_profile
        category_mapping = {'1':'D', '2':'E', '3':'F', '4':'G'}
        level = "level_{}_{}_{}".format(
          category_mapping[request.POST['category']],
          request.POST['subcategory'],
          request.POST['subsubcategory'])
        setattr(profile, level, request.POST['level'])
        profile.save()
        return HttpResponseRedirect("{}#categorie-2-{}-{}-{}".format(
                reverse('theory'),
                request.POST['category'],
                request.POST['subcategory'],
                request.POST['subsubcategory']))
    else:
        raise Http404("Deze webpagina bestaat niet!")

@login_required
def update_pi_profile(request):
    if has_group(request.user, "Leerling"):
        profile = request.user.user_profile.professional_identity_profile
        form = UserForm(request.POST)
        if form.is_valid():
            if request.POST['answer-nr'] == "answer_q1":
                setattr(profile, "answer_q1", form.cleaned_data['answer_q1'])
                profile.save()
                return HttpResponseRedirect("{}#categorie-3-1".format(reverse('theory')))
            else :
                setattr(profile, "answer_q2", form.cleaned_data['answer_q2'])
                profile.save()
                return HttpResponseRedirect("{}#categorie-3-2".format(reverse('theory')))
    else:
        raise Http404("Deze webpagina bestaat niet!")


@login_required
def update_notes(request):
    if has_group(request.user, "Leerling"):
        notes = request.user.user_profile.category_notes
        note_form = NoteForm(request.POST)
        if note_form.is_valid():
            category_mapping = {
                '1-1' : 'a',
                '1-2' : 'b',
                '1-3' : 'c',
                '2-1' : 'd',
                '2-2' : 'e',
                '2-3' : 'f',
                '2-4' : 'g',
            }
            numeric_cat = request.POST['note_category']
            cat = category_mapping[numeric_cat]
            note_cat = "cat_{}_note".format(cat)
            new_note = note_form.cleaned_data[note_cat]
            setattr(notes, note_cat, new_note)
            notes.save()
        return HttpResponseRedirect("{}#categorie-{}".format(reverse('theory'), numeric_cat))
    else:
        return Http404("Deze webpagina bestaat niet!")


@login_required
def shared_profiles(request):
    if has_group(request.user, "Docent"):
        profiles = request.user.accessable_user_profile.filter(profile_owner__is_active=True)
        context = {
            'accessible_profiles': profiles,
        }
        return render(request, 'webapp/shared_profiles.html', context)
    else:
        raise Http404("Deze webpagina bestaat niet!")


@login_required
def view_shared_profile(request):
    if has_group(request.user, "Docent"):
        dimensions = LKL_Dimension.objects.all()
        profile = User_Profile.objects.get(pk=int(request.POST['profile_id']));
        categories = LKL_Category.objects.all()
        subsubcategories = LKL_Subsubcategory.objects.all()

        _, _, ps_subsubcategories = get_subsubcategories(1)
        _, _, bpb_subsubcategories = get_subsubcategories(2)
        ps_profile = get_profile_data(profile.primary_skills_profile, ps_subsubcategories)
        bpb_profile = get_profile_data(profile.broad_professional_basis_profile, bpb_subsubcategories)
        context = {
            "profile" : profile,
            "ps_profile" : ps_profile,
            "bpb_profile" : bpb_profile,
            "categories" : categories,
            "dimensions" : dimensions,
        }
        return render(request, 'webapp/shared_profile.html', context)
    else:
        raise Http404("Deze webpagina bestaat niet!")


@login_required
def theory(request):
    profile = request.user.user_profile
    dimensions = LKL_Dimension.objects.all()
    categories = LKL_Category.objects.all()
    subcategories = LKL_Subcategory.objects.all()
    subsubcategories = LKL_Subsubcategory.objects.all()
    _, _, ps_subsubcategories = get_subsubcategories(1)
    _, _, bpb_subsubcategories = get_subsubcategories(2)
    ps_profile = get_profile_data(profile.primary_skills_profile, ps_subsubcategories)
    bpb_profile = get_profile_data(profile.broad_professional_basis_profile, bpb_subsubcategories)
    user_pi_profile = request.user.user_profile.professional_identity_profile
    user_notes =  request.user.user_profile.category_notes
    user_form = UserForm()
    user_form.fields['answer_q1'].initial = user_pi_profile.answer_q1
    user_form.fields['answer_q2'].initial = user_pi_profile.answer_q2
    note_form = NoteForm()
    note_form.fields['cat_a_note'].initial = user_notes.cat_a_note
    note_form.fields['cat_b_note'].initial = user_notes.cat_b_note
    note_form.fields['cat_c_note'].initial = user_notes.cat_c_note
    note_form.fields['cat_d_note'].initial = user_notes.cat_d_note
    note_form.fields['cat_e_note'].initial = user_notes.cat_e_note
    note_form.fields['cat_f_note'].initial = user_notes.cat_f_note
    note_form.fields['cat_g_note'].initial = user_notes.cat_g_note
    context = {
        'dimensions' : dimensions,
        'categories' : categories,
        'subcategories' : subcategories,
        'subsubcategories' : subsubcategories,
        'ps_profile' : ps_profile,
        'bpb_profile' : bpb_profile,
        'user_form' : user_form,
        'user_notes' : user_notes,
        'note_form' : note_form,
    }
    return render(request, 'webapp/theory.html', context)


@login_required
def manage_accounts(request):
    if (request.user.is_superuser):
        accounts = User.objects.all();
        context = {
            'accounts' : accounts,
        }
        return render(request, 'webapp/manage_accounts.html', context)
    else:
        raise Http404("Deze webpagina bestaat niet!")


@login_required
def manage_students(request, newContext={}):
    if (request.user.is_superuser):
        if ('form' not in newContext.keys()):
            form = NewStudentForm();
        else:
            form = newContext['form']

        context = {
            'form' : form,
        }
        return render(request, 'webapp/manage_students.html', context)
    else:
        raise Http404("Deze webpagina bestaat niet!")


@login_required
def manage_teachers(request, newContext={}):
    if (request.user.is_superuser):
        if ('form' not in newContext.keys()):
            form = NewTeacherForm();
        else:
            form = newContext['form']

        context = {
            'form' : form,
        }
        return render(request, 'webapp/manage_teachers.html', context)
    else:
        raise Http404("Deze webpagina bestaat niet!")


@login_required
def create_students(request):
    if (request.user.is_superuser):
        form = NewStudentForm(request.POST)
        if form.is_valid():
            studentname = form.cleaned_data['studentnaam']
            student_id = form.cleaned_data['studentId']
            email = form.cleaned_data['email']
            generatedPassword = User.objects.make_random_password()
            newUser = User.objects.create_user(
                username = studentname,
                password = generatedPassword,
                email = email
            )
            newUser.save()
            newUser.user_profile.student_id = student_id
            newUser.user_profile.save()
            studentGroup = Group.objects.get(name="Leerling")
            studentGroup.user_set.add(newUser)
            send_mail(
                'Log in met je leerkrachtlijn account',
                """
Beste student, er is voor jou een account aangemaakt op amsterdamseleerkrachtlijn.nl.
Login kan met de volgende gegevens: \n
Gebruikersnaam: {} \n
Wachtwoord: {}
                """.format(studentname, generatedPassword),
                'webmaster@localhost',
                [request.POST['email']],
                fail_silently=False,
            )
            return HttpResponseRedirect(reverse('manage_students'))
        return manage_students(request, {'form': form})
    else:
        raise Http404("Deze webpagina bestaat niet!")


@login_required
def create_teachers(request):
    if (request.user.is_superuser):
        form = NewTeacherForm(request.POST)
        if form.is_valid():
            teachername = form.cleaned_data['docentnaam']
            email = form.cleaned_data['email']
            generatedPassword = User.objects.make_random_password()
            newUser = User.objects.create_user(
                username = teachername,
                password = generatedPassword,
                email = email
            )
            newUser.save()
            teacherGroup = Group.objects.get(name="Docent")
            teacherGroup.user_set.add(newUser)
            send_mail(
                'Log in met je leerkrachtlijn account',
                """
Beste docent, er is voor jou een account aangemaakt op amsterdamseleerkrachtlijn.nl.
Login kan met de volgende gegevens: \n
Gebruikersnaam: {} \n
Wachtwoord: {}
                """.format(teachername, generatedPassword),
                'webmaster@localhost',
                [request.POST['email']],
                fail_silently=False,
            )
            return HttpResponseRedirect(reverse('manage_teachers'))
        return manage_students(request, {'form': form})
    else:
        raise Http404("Deze webpagina bestaat niet!")

def get_profile_data(profile, subsubcategories):
    profile_categories = profile._meta.get_fields()[2:]
    profile_data = []
    for i in range(0, len(subsubcategories)):
         field = profile_categories[i]
         fieldvalue = field.value_from_object(profile)
         profile_data.append((subsubcategories[i], field.name, fieldvalue))
    return profile_data


def get_subsubcategories(dimension_pk):
    dimension = LKL_Dimension.objects.get(pk=dimension_pk)
    categories = LKL_Category.objects.filter(super_category=dimension)
    subcategories = LKL_Subcategory.objects.filter(super_category__in=categories)
    subsubcategories = LKL_Subsubcategory.objects.filter(super_category__in=subcategories)
    return (categories, subcategories, subsubcategories)


def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists()
