from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('theorie/', views.theory, name='theory'),
    path('gedeelde_profielen/', views.shared_profiles, name='shared_profiles'),
    path('gedeelde_profielen/profiel', views.view_shared_profile, name='view_shared_profile'),
    path('profiel/', views.profile, name='profile'),
    path('profiel/update_email', views.update_email, name='update_email'),
    path('profiel/deel_profiel', views.share_profile, name='share_profile'),
    path('profiel/update_profiel/primaire_proces', views.update_ps_profile, name='update_ps_profile'),
    path('profiel/update_profiel/brede_professionele_basis', views.update_bpb_profile, name='update_bpb_profile'),
    path('profiel/update_profiel/professionele_identiteit', views.update_pi_profile, name='update_pi_profile'),
]
