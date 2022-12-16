from django.views.generic import DetailView
from .models import Company


class CompanyInfoView(DetailView):
    model = Company
    queryset = Company.objects.filter(is_active=True)
    template_name = 'company/company_info.html'
