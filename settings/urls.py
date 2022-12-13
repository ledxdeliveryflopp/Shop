from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
  path('admin/', admin.site.urls),
  path('shop/', include('shop.urls', namespace='shop')),
  path('company/', include('company.urls', namespace='company')),
  path('user/', include('user.urls', namespace='user')),
  path('accounts/', include('django.contrib.auth.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) +\
              static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
