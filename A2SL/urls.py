from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('signup/',views.signup_view,name='signup'),
    path('animation/',views.animation_view,name='animation'),
    path('',views.home_view,name='home'),
    path('animation/',views.animation_view,name='animation')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
