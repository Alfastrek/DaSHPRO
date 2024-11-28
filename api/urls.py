from django.urls import path
from . import views

urlpatterns = [
    # API endpoints
    path('country_intensity_datas/', views.country_intensity_datas, name='countryintensitydatas'),
    path('datas/', views.datas, name='datas'),
    path('relevance_pestle_datas/', views.relevance_pestle_datas, name='relevancepestledatas'),

    # Dashboard pages
    path('', views.base, name='base'),
    path("reports", views.reports, name="dashboard-reports"),
    path("datatables", views.datatables, name="dashboard-datatables"),
    path("profile", views.profile, name="dashboard-profile"),
]
