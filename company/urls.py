from django.urls import path

from .views import AllCompanyView

app_name = 'company'

urlpatterns = [
    path('<int:pk>/', AllCompanyView.as_view(), name='all_company'),
]
