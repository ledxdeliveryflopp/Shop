from django.views.generic import ListView

from .models import Product


class IndexView(ListView):
    model = Product
    template_name = 'index.html'
    queryset = Product.objects.filter(is_active=True)


