from django.views.generic import ListView

from .models import Product


class IndexView(ListView):
    model = Product
    queryset = Product.objects.filter(is_active=True)
    template_name = 'index.html'

