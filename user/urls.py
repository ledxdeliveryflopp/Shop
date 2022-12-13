from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import SignUp, UserLogin, LogoutView, PersonalArea

app_name = 'user'

urlpatterns = [
    path('registration/', SignUp.as_view(), name='registration'),
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('user/', PersonalArea.as_view(), name='personal_area'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
