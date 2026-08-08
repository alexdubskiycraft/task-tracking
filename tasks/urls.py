from django.urls import path
from tasks import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.index, name="index"),
    path("signup/", views.signup_page, name="signup"),
    path("login/", views.login_page, name="login"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('tasks/', views.TaskList.as_view(), name="task_list"),
    path('tasks/create/', views.TaskCreate.as_view(), name="task_create"),
    path("tasks/view/<slug:slug>/", views.TaskDetail.as_view(), name="task_detail"),
]