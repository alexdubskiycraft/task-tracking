from django.urls import path
from tasks import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.index, name="index"),
    path("signup/", views.signup_page, name="signup"),
    path("login/", views.login_page, name="login"),
    path('logout/', LogoutView.as_view(), name='logout'),
]