from django.urls import path
from tasks import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.TaskList.as_view(), name="task_list"),
    path("signup/", views.signup_page, name="signup"),
    path("login/", views.login_page, name="login"),
    path('logout/', LogoutView.as_view(), name='logout'),
    #path('tasks/', views.TaskList.as_view(), name="task_list"),
    path('tasks/create/', views.TaskCreate.as_view(), name="task_create"),
    path("tasks/view/<slug:slug>/", views.TaskDetail.as_view(), name="task_detail"),
    path("tasks/delete/<slug:slug>/", views.TaskDelete.as_view(), name="task_delete"),
    path("tasks/update/<slug:slug>/", views.TaskUpdate.as_view(), name="task_update"),
]