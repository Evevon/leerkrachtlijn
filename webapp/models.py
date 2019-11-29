'''
This file contains all django database models in this project.
A database model is similar to a python class, and corresponds
to a database table with table fields.
'''
from django.conf import settings
from datetime import datetime
from django.db import models


class LKL_Dimension(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=50)
    short_description = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class LKL_Category(models.Model):
    super_category = models.ForeignKey('LKL_Dimension', on_delete=models.CASCADE)
    number = models.IntegerField()
    name = models.CharField(max_length=50)
    short_description = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class LKL_Subcategory(models.Model):
    super_category = models.ForeignKey('LKL_Category', on_delete=models.CASCADE)
    number = models.IntegerField()
    name = models.CharField(max_length=50)
    short_description = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class LKL_Subsubcategory(models.Model):
    super_category = models.ForeignKey('LKL_Subcategory', on_delete=models.CASCADE)
    number = models.IntegerField()
    name = models.CharField(max_length=50)
    short_description = models.CharField(max_length=100)
    description_beginning = models.TextField()
    description_in_development = models.TextField()
    description_starter = models.TextField()
    description_basic_competence = models.TextField()
    description_professional_competence = models.TextField()

    def __str__(self):
        return self.name


class LKL_Resource(models.Model):
    categories = models.ManyToManyField(LKL_Subcategory);
    title = models.CharField(max_length=300)
    upva_resource = models.BooleanField(default=False)
    hva_resource = models.BooleanField(default=False)
    reference = models.CharField(max_length=500)
    resource_URL = models.URLField()
    def __str__(self):
        return self.title


class User_Profile(models.Model):
    profile_owner = models.OneToOneField(settings.AUTH_USER_MODEL,
      related_name='user_profile',
      on_delete=models.CASCADE)
    student_id = models.CharField(max_length=20, blank=True)
    profile_shared_list = models.ManyToManyField(settings.AUTH_USER_MODEL,
      related_name='accessable_user_profile',
      limit_choices_to={'groups__name': 'Docent'}, blank=True)
    def __str__(self):
        return "{}".format(self.profile_owner)


class Category_Notes(models.Model):
    user_profile = models.OneToOneField(User_Profile, on_delete=models.CASCADE)
    cat_a_note = models.TextField(blank=True)
    cat_b_note = models.TextField(blank=True)
    cat_c_note = models.TextField(blank=True)
    cat_d_note = models.TextField(blank=True)
    cat_e_note = models.TextField(blank=True)
    cat_f_note = models.TextField(blank=True)
    cat_g_note = models.TextField(blank=True)

    def __str__(self):
        return "{}".format(self.user_profile.profile_owner)


class Primary_Skills_Profile(models.Model):
    user_profile = models.OneToOneField(User_Profile, on_delete=models.CASCADE)
    NO_LEVEL = 'N'
    BEGINNER = 'B'
    IN_DEVELOPMENT = 'IO'
    STARTER = 'S'
    BASIC_COMPETENCE = 'BC'
    PROFESSIONAL_COMPETENCE = 'PC'
    LEVEL_OPTIONS = [
        (NO_LEVEL, 'Geen niveau'),
        (BEGINNER, 'Beginnend'),
        (IN_DEVELOPMENT, 'In Ontwikkeling'),
        (STARTER, 'Startbekwaam'),
        (BASIC_COMPETENCE, 'Basisbekwaam'),
        (PROFESSIONAL_COMPETENCE, 'Vakbekwaam'),
    ]
    level_A_1_1 = models.CharField(max_length=2, choices=LEVEL_OPTIONS, default=NO_LEVEL)
    level_A_1_2 = models.CharField(max_length=2, choices=LEVEL_OPTIONS, default=NO_LEVEL)
    level_A_2_1 = models.CharField(max_length=2, choices=LEVEL_OPTIONS, default=NO_LEVEL)
    level_A_2_2 = models.CharField(max_length=2, choices=LEVEL_OPTIONS, default=NO_LEVEL)
    level_A_3_1 = models.CharField(max_length=2, choices=LEVEL_OPTIONS, default=NO_LEVEL)
    level_A_3_2 = models.CharField(max_length=2, choices=LEVEL_OPTIONS, default=NO_LEVEL)
    level_B_1_1 = models.CharField(max_length=2, choices=LEVEL_OPTIONS, default=NO_LEVEL)
    level_B_1_2 = models.CharField(max_length=2, choices=LEVEL_OPTIONS, default=NO_LEVEL)
    level_B_2_1 = models.CharField(max_length=2, choices=LEVEL_OPTIONS, default=NO_LEVEL)
    level_B_2_2 = models.CharField(max_length=2, choices=LEVEL_OPTIONS, default=NO_LEVEL)
    level_B_3_1 = models.CharField(max_length=2, choices=LEVEL_OPTIONS, default=NO_LEVEL)
    level_B_3_2 = models.CharField(max_length=2, choices=LEVEL_OPTIONS, default=NO_LEVEL)
    level_C_1_1 = models.CharField(max_length=2, choices=LEVEL_OPTIONS, default=NO_LEVEL)
    level_C_1_2 = models.CharField(max_length=2, choices=LEVEL_OPTIONS, default=NO_LEVEL)
    level_C_2_1 = models.CharField(max_length=2, choices=LEVEL_OPTIONS, default=NO_LEVEL)
    level_C_2_2 = models.CharField(max_length=2, choices=LEVEL_OPTIONS, default=NO_LEVEL)
    level_C_3_1 = models.CharField(max_length=2, choices=LEVEL_OPTIONS, default=NO_LEVEL)
    level_C_3_2 = models.CharField(max_length=2, choices=LEVEL_OPTIONS, default=NO_LEVEL)

    def __str__(self):
        return "{}".format(self.user_profile.profile_owner)


class Broad_Professional_Basis_Profile(models.Model):
    user_profile = models.OneToOneField(User_Profile, on_delete=models.CASCADE)
    NO_LEVEL = 'N'
    BEGINNER = 'B'
    IN_DEVELOPMENT = 'IO'
    STARTER = 'S'
    BASIC_COMPETENCE = 'BC'
    PROFESSIONAL_COMPETENCE = 'PC'
    LEVEL_OPTIONS = [
        (NO_LEVEL, 'Geen niveau'),
        (BEGINNER, 'Beginnend'),
        (IN_DEVELOPMENT, 'In Ontwikkeling'),
        (STARTER, 'Startbekwaam'),
        (BASIC_COMPETENCE, 'Basisbekwaam'),
        (PROFESSIONAL_COMPETENCE, 'Vakbekwaam'),
    ]
    level_D_1_1 = models.CharField(max_length=2, choices=LEVEL_OPTIONS, default=NO_LEVEL)
    level_D_1_2 = models.CharField(max_length=2, choices=LEVEL_OPTIONS, default=NO_LEVEL)
    level_D_2_1 = models.CharField(max_length=2, choices=LEVEL_OPTIONS, default=NO_LEVEL)
    level_D_2_2 = models.CharField(max_length=2, choices=LEVEL_OPTIONS, default=NO_LEVEL)
    level_D_3_1 = models.CharField(max_length=2, choices=LEVEL_OPTIONS, default=NO_LEVEL)
    level_D_3_2 = models.CharField(max_length=2, choices=LEVEL_OPTIONS, default=NO_LEVEL)
    level_E_1_1 = models.CharField(max_length=2, choices=LEVEL_OPTIONS, default=NO_LEVEL)
    level_E_1_2 = models.CharField(max_length=2, choices=LEVEL_OPTIONS, default=NO_LEVEL)
    level_E_2_1 = models.CharField(max_length=2, choices=LEVEL_OPTIONS, default=NO_LEVEL)
    level_E_2_2 = models.CharField(max_length=2, choices=LEVEL_OPTIONS, default=NO_LEVEL)
    level_E_3_1 = models.CharField(max_length=2, choices=LEVEL_OPTIONS, default=NO_LEVEL)
    level_E_3_2 = models.CharField(max_length=2, choices=LEVEL_OPTIONS, default=NO_LEVEL)
    level_F_1_1 = models.CharField(max_length=2, choices=LEVEL_OPTIONS, default=NO_LEVEL)
    level_F_1_2 = models.CharField(max_length=2, choices=LEVEL_OPTIONS, default=NO_LEVEL)
    level_F_2_1 = models.CharField(max_length=2, choices=LEVEL_OPTIONS, default=NO_LEVEL)
    level_F_2_2 = models.CharField(max_length=2, choices=LEVEL_OPTIONS, default=NO_LEVEL)
    level_F_3_1 = models.CharField(max_length=2, choices=LEVEL_OPTIONS, default=NO_LEVEL)
    level_G_1_1 = models.CharField(max_length=2, choices=LEVEL_OPTIONS, default=NO_LEVEL)
    level_G_1_2 = models.CharField(max_length=2, choices=LEVEL_OPTIONS, default=NO_LEVEL)
    level_G_2_1 = models.CharField(max_length=2, choices=LEVEL_OPTIONS, default=NO_LEVEL)
    level_G_2_2 = models.CharField(max_length=2, choices=LEVEL_OPTIONS, default=NO_LEVEL)
    level_G_3_1 = models.CharField(max_length=2, choices=LEVEL_OPTIONS, default=NO_LEVEL)
    level_G_3_2 = models.CharField(max_length=2, choices=LEVEL_OPTIONS, default=NO_LEVEL)

    def __str__(self):
        return "{}".format(self.user_profile.profile_owner)


class Professional_Identity_Profile(models.Model):
    user_profile = models.OneToOneField(User_Profile, on_delete=models.CASCADE)
    answer_q1 = models.TextField(blank=True)
    answer_q2 = models.TextField(blank=True)

    def __str__(self):
        return "{}".format(self.user_profile.profile_owner)
