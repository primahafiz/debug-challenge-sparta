from django.contrib.auth import logout
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from .forms import TaskForm
from .models import TaskModel
from django.utils import timezone

# Create your views here.

def index(request):
    if(not(request.user.is_authenticated)):
        return redirect('/signin')
    else:
        if(request.method=='POST'):
            logout(request)
            return redirect('/signin')
        datetime_now=timezone.now()
        tasks=TaskModel.objects.filter(pengguna=request.user,waktu__gte=datetime_now).order_by('waktu')
        context={
            'tasks':tasks
        }
        return render(request,'index.html',context)

def addPage(request):
    task_form=TaskForm(request.POST or None)
    if(request.method=="POST"):
        if(task_form.is_valid()):
            task_form.save(user=request.user)
            return redirect('/')
    context={
        'add_form':task_form
    }

    return render(request,'addPage.html',context)

def delete_task(request,task_id):
    task=TaskModel.objects.get(pk=task_id)
    task.delete()
    return redirect('/')