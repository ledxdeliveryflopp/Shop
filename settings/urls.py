from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
  path('admin/', admin.site.urls),
  path('shop/', include('shop.urls', namespace='shop')),
  path('', RedirectView.as_view(url='shop/', permanent=True)),
  path('company/', include('company.urls', namespace='company')),
  path('user/', include('user.urls', namespace='user')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) +\
              static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
