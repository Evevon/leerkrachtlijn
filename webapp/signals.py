from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from webapp.models import User_Profile, Primary_Skills_Profile, Broad_Professional_Basis_Profile, Professional_Identity_Profile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        new_user_profile = User_Profile.objects.create(profile_owner=instance)
        new_user_profile.save()


@receiver(post_save, sender=User_Profile)
def create_ps_profile(sender, instance, created, **kwargs):
    if created:
        new_ps_profile = Primary_Skills_Profile.objects.create(user_profile=instance)
        new_ps_profile.save()


@receiver(post_save, sender=User_Profile)
def create_bpb_profile(sender, instance, created, **kwargs):
    if created:
        new_bpb_profile = Broad_Professional_Basis_Profile.objects.create(user_profile=instance)
        new_bpb_profile.save()


@receiver(post_save, sender=User_Profile)
def create_pi_profile(sender, instance, created, **kwargs):
    if created:
        new_pi_profile = Professional_Identity_Profile.objects.create(user_profile=instance)
