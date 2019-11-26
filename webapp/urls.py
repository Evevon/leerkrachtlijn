from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mijn_leerkrachtlijn/', views.theory, name='theory'),
    path('gedeelde_profielen/', views.shared_profiles, name='shared_profiles'),
    path('gedeelde_profielen/profiel', views.view_shared_profile, name='view_shared_profile'),
    path('profiel/', views.profile, name='profile'),
    path('profiel/instellingen', views.profile_settings, name='profile_settings'),
    path('profiel/update_email', views.update_email, name='update_email'),
    path('profiel/deel_profiel', views.share_profile, name='share_profile'),
    path('mijn_leerkrachtlijn/update/primaire_proces', views.update_ps_profile, name='update_ps_profile'),
    path('mijn_leerkrachtlijn/update/brede_professionele_basis', views.update_bpb_profile, name='update_bpb_profile'),
    path('mijn_leerkrachtlijn/update/professionele_identiteit', views.update_pi_profile, name='update_pi_profile'),
    path('manage_accounts/', views.manage_accounts, name='manage_accounts'),
    path('manage_accounts/manage_leerlingen/', views.manage_students, name='manage_students'),
    path('manage_accounts/manage_docenten/', views.manage_teachers, name='manage_teachers'),
    path('manage_accounts/leerling_aanmaken/', views.create_students, name='create_students'),
    path('manage_accounts/docent_aanmaken/', views.create_teachers, name='create_teachers'),
    path('wachtwoord_aanpassen/', views.change_password, name='change_password'),
    path('manage_accounts/update_accounts', views.update_active, name='update_active'),
]
