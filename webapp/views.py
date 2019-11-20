from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
from .models import *


class UserForm(forms.Form):
    user_email = forms.EmailField(required=False)
    answer_q1 = forms.CharField(widget=forms.Textarea(attrs={"rows":8, "cols":80}), required=False)
    answer_q2 = forms.CharField(widget=forms.Textarea(attrs={"rows":8, "cols":80}), required=False)


@login_required
def index(request):
    context = {}
    return render(request, 'webapp/index.html', context)


@login_required
def profile(request):
    if has_group(request.user, "Leerling"):
        dimensions = LKL_Dimension.objects.all()
        categories = LKL_Category.objects.all()
        subcategories = LKL_Subcategory.objects.all()
        subsubcategories = LKL_Subsubcategory.objects.all()
        user_ps_profile = request.user.user_profile.primary_skills_profile
        user_bpb_profile = request.user.user_profile.broad_professional_basis_profile
        user_pi_profile = request.user.user_profile.professional_identity_profile

        ps_categories, _, ps_subsubcategories = get_subsubcategories(1)
        bpb_categories, _, bpb_subsubcategories = get_subsubcategories(2)
        ps_profile_data = get_profile_data(user_ps_profile, ps_subsubcategories)
        bpb_profile_data = get_profile_data(user_bpb_profile, bpb_subsubcategories)

        all_teachers = User.objects.filter(groups__name='Docent')
        user_form = UserForm()
        user_form.fields['answer_q1'].initial = user_pi_profile.answer_q1
        user_form.fields['answer_q2'].initial = user_pi_profile.answer_q2
        context = {
            'dimensions' : dimensions,
            'categories' : categories,
            'ps_categories' : ps_categories,
            'bpb_categories' : bpb_categories,
            'subcategories' : subcategories,
            'subsubcategories' : subsubcategories,
            'ps_profile' : ps_profile_data,
            'bpb_profile' : bpb_profile_data,
            'pi_profile' : user_pi_profile,
            'all_teachers' : all_teachers,
            'user_form': user_form,
        }
        return render(request, 'webapp/profile.html', context)
    else:
        raise Http404("Deze webpagina bestaat niet!")


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
        return HttpResponseRedirect(reverse('profile'))
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

        return HttpResponseRedirect("{}#dimensie-1".format(reverse('profile')))
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
        return HttpResponseRedirect("{}#dimensie-2".format(reverse('profile')))
    else:
        raise Http404("Deze webpagina bestaat niet!")

@login_required
def update_pi_profile(request):
    if has_group(request.user, "Leerling"):
        profile = request.user.user_profile.professional_identity_profile
        form = UserForm(request.POST)
        if form.is_valid():
            if request.POST['answer-nr'] == "answer_q1":
                setattr(profile, request.POST['answer-nr'], form.cleaned_data['answer_q1'])
            else :
                print(form.cleaned_data['answer_q2'])
                setattr(profile, request.POST['answer-nr'], form.cleaned_data['answer_q2'])
            profile.save()
        return HttpResponseRedirect("{}#dimensie-3".format(reverse('profile')))
    else:
        raise Http404("Deze webpagina bestaat niet!")


@login_required
def shared_profiles(request):
    if has_group(request.user, "Docent"):
        context = {}
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
    dimensions = LKL_Dimension.objects.all()
    categories = LKL_Category.objects.all()
    subcategories = LKL_Subcategory.objects.all()
    subsubcategories = LKL_Subsubcategory.objects.all()
    context = {
        'dimensions' : dimensions,
        'categories' : categories,
        'subcategories' : subcategories,
        'subsubcategories' : subsubcategories,
    }
    return render(request, 'webapp/theory.html', context)


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
