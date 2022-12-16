from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import SignUp, UserLogin, LogoutView, PersonalArea, UpdateUser, DeleteUser

app_name = 'user'

urlpatterns = [
    path('registration/', SignUp.as_view(), name='registration'),
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('user/', PersonalArea.as_view(), name='personal_area'),
    path('user-update/<int:pk>/', UpdateUser.as_view(), name='update_user'),
    path('user-delete/<int:pk>/', DeleteUser.as_view(), name='delete_user'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
