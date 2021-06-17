from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterform,Userupdateform,profileupdateform
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserRegisterform(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data.get('username')
            messages.success(request,f'Your Account has been created you now able to login')
            return  redirect('login')
    else:
        form =UserRegisterform()
    return  render(request,'users/register.html',{'form':form})
@login_required
def profile(request):
    if request.method == 'POST':
        u_form=Userupdateform(request.POST, instance=request.user)
        p_form=profileupdateform(request.POST,request.FILES,
                                 instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your Account has been updated!')
            return redirect('profile')
    else:
        u_form = Userupdateform(instance=request.user)
        p_form = profileupdateform(instance=request.user.profile)

    context={
        'u_form':u_form,
        'p_form':p_form,
    }
    return render(request,'users/profile.html',context)

