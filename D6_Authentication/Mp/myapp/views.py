from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from myapp.models import UserMoreInfo
from django.contrib.auth.models import User
from myapp.forms import UserForm,UserMoreInfoForm 
from django.urls import reverse


# ___________________________________________________User Login Libeary ____________________________________________
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required




# Create your views here.



def index(request):
    dic={}
    if request.user.is_authenticated:
        current_user = request.user
        user_id=current_user.id
        userInfo=User.objects.get(pk=user_id)
        userMoreInfo=UserMoreInfo.objects.get(user__pk=user_id)
        dic={'iuserInfo':userInfo,'iuserMoreInfo':userMoreInfo }
    return render(request, 'myapp/index.html',context=dic)


def Register(request):
    register=False
    if request.method == 'POST':
        userForm=UserForm(data=request.POST)
        userInfoForm=UserMoreInfoForm(data=request.POST)
        if userForm.is_valid() and userInfoForm.is_valid():
            nuser=userForm.save()
            nuser.set_password(nuser.password)
            nuser.save()
            userInfo=userInfoForm.save(commit=False)
            userInfo.user=nuser
            if 'Profile_Picture' in request.FILES:
                userInfo.Profile_Picture=request.FILES['Profile_Picture']
                print('here')
            userInfo.save()
            register=True
            
    else:
        userForm=UserForm()
        userInfoForm=UserMoreInfoForm()
    return render(request,'myapp/register.html',{'userForm':userForm,'userInfoForm':userInfoForm,'register':register})



# _________________________________________________________________________for User Login ____________________________________________________________________________

def Ulog(request):
    return render(request,'myapp/ulogin.html',{})


def UserLogin(request):
    if request.method == 'POST':
        Fusername=request.POST.get('UserName')
        Fpassword=request.POST.get('UserPassword')
        user=authenticate(username=Fusername,password=Fpassword)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('relative:index'))
                # return render(request,'myapp/index.html',{})
            else:
                return HttpResponse('Account is not active')
        
        else:
            return HttpResponse('Invalid Login Details')
        
    else:
        return render(request,'myapp/ulogin.html',{})


@login_required
def Out(request):
    logout(request)
    return HttpResponseRedirect(reverse('relative:ulogin'))
    # return render(request,'myapp/index.html',{})
