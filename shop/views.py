from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView
from .forms import CreateProductForm
from .models import Product


class IndexView(ListView):
    model = Product
    template_name = 'index.html'


class CreateProductView(LoginRequiredMixin, CreateView):
    login_url = 'user:login'
    model = Product
    template_name = 'shop/create_product.html'
    form_class = CreateProductForm
    success_url = reverse_lazy('user:personal_area')


class DeleteProductView(DeleteView):
    model = Product
    success_url = reverse_lazy('shop:index')

    def form_valid(self):
        self.object.delete()



