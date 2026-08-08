from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from tasks.models import *
from django.db.models import Q
from .forms import TaskFilterForm, TaskForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin



def signup_page(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})    

def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})  

@login_required
def index(request):
    context = {
        "render_string": "Hello, guest!"
    }
    return render(request, "index.html", context)

class TaskList(ListView):
    model = Task
    template_name = "task/task_list.html"
    context_object_name = "tasks"
    paginate_by = 5

    def get_queryset(self):
        qs = Task.objects.all()
        q = self.request.GET.get("q") or ""
        status = self.request.GET.get("status") or ""
        priority = self.request.GET.get("priority") or ""
        if q:
            qs = qs.filter(Q(name__icontains=q))
        if status:
            qs = qs.filter(status=status)
        if priority:
            qs = qs.filter(priority=priority)
        return qs.select_related("user")

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["filter_form"] = TaskFilterForm(self.request.GET or None)
        return ctx


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm 
    template_name = "tasks/task_form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("task_detail", kwargs={"id": self.object.id})

class TaskDetail(DetailView):
    model = Task
    template_name = "tasks/task_detail.html"
    context_object_name = "task"
    slug_field = "id"
    slug_url_kwarg = "id"    
    
