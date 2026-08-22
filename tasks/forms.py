from django import forms
from  .models import Task

class TaskFilterForm(forms.Form):
    q = forms.CharField(required=False, widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "пошук"}))
    status = forms.ChoiceField(required=False, choices=[("", "Будь-який")] + list(Task.Status.choices), widget=forms.Select(attrs={"class": "form-select"}))
    priority = forms.ChoiceField(required=False, choices=[("", "Будь-який")] + [(p.value, p.label) for p in Task.Priority], widget=forms.Select(attrs={"class": "form-select"}))

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task   
        fields = ["name", "description", "status", "priority", "end_date", "image"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 6}),
            "status": forms.Select(attrs={"class": "form-select"}), 
            "priority": forms.Select(attrs={"class": "form-select"}),
            "end_date": forms.DateTimeInput(attrs={"class": "form-control datepicker"}),
            "image": forms.ClearableFileInput(attrs={"class": "form_control", "accept": "image/*"}),
        }