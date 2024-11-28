from django.urls import path
from django.shortcuts import redirect
from . import views

# Redirect root URL to external URL
def root_redirect(request):
    return redirect('https://dashpro.azurewebsites.net/', permanent=True)  # Permanent redirect to the new URL

urlpatterns = [
    path('', root_redirect),  # Redirect '/' to the external URL
    path('country_intensity_datas/', views.country_intensity_datas, name='countryintensitydatas'),
    path('datas/', views.datas, name='datas'),
    path('relevance_pestle_datas/', views.relevance_pestle_datas, name='relevancepestledatas'),
    path('reports', views.reports, name='dashboard-reports'),
    path('datatables', views.datatabels, name='dashboard-datatables'),
    path('profile', views.profile, name='dashboard-profile'),
]
