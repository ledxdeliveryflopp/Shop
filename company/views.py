from django.views.generic import ListView

from .models import Company


class AllCompanyView(ListView):
    model = Company
    queryset = Company.objects.filter(is_active=True)
    # template_name = 'company/all_company.html'
