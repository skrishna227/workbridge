from django.urls import path
from . import views

urlpatterns = [
    path('', views.CompanyList.as_view(), name='company-list'),
    path('registration/', views.CompanyRegistrationView.as_view(), name='company-registration'),
    
]