from django.contrib.auth.decorators import permission_required
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import IndexView, CreateProductView, DeleteProductView

app_name = 'shop'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('create-product/', CreateProductView.as_view(), name='create_product'),
    path('delete-product/<int:pk>/', permission_required('change-post', login_url='user:login')(
        DeleteProductView.as_view()),
         name='delete_product'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
