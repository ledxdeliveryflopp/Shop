from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import Register

app_name = 'user'

urlpatterns = [
    path('registration/', Register.as_view(), name='registration'),
    # path('personal_area/', PersonalAreaView.as_view(), name='personal_area'),
    # path('delete_user/<int:pk>/', DeleteUserView.as_view(), name='delete_user'),
    # path('update_user/<int:pk>/', UpdateUser.as_view(), name='update_user'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
