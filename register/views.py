from django.shortcuts import render, redirect 
from .forms import MyUserForm
from django.contrib import messages

# Create your views here.

def registerView(request):
    if(request.user.is_authenticated):
        return redirect('/')
    else:
        form=MyUserForm
        if(request.method=='POST'):
            form=MyUserForm(request.POST)
            if(form.is_valid()):
                form.save()
                user=form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('/signin')
        context={
            'form':form,
        }

        return render(request,'registerPage.html',context)
