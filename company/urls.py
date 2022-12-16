from django.urls import path
from .views import CompanyInfoView

app_name = 'company'

urlpatterns = [
    path('company/<int:pk>/', CompanyInfoView.as_view(), name='company_info'),
]

