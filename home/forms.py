from django import forms
from django.forms import widgets
from .models import TaskModel
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget, AdminSplitDateTime

class TaskForm(forms.ModelForm):
    waktu=forms.SplitDateTimeField(widget=AdminSplitDateTime())
    class Meta:
        model=TaskModel
        fields = '__all__'
        exclude = ('pengguna',)
    def save(self,user=None,commit=True):
        q=super(TaskForm,self).save(commit=False)
        q.pengguna=user
        if commit:
            q.save()
        return q
        