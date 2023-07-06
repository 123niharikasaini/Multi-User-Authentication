from django.shortcuts import render,HttpResponse,redirect
from .form import SignUpForm,LoginForm
from django.contrib.auth import authenticate,login

# Create your views here.
def index(request):
    return HttpResponse("working")

def register(request):
    msg=None
    if request.method=="POST":
        form=SignUpForm(request.POST) #call signUpForm
        if form.is_valid():# check validity
            user=form.save()
            msg="user created"
            return redirect('login_view')
        else:
            msg='form is not valid'
    
    else:
        form=SignUpForm()
    return render(request,'register.html',{'form': form,'msg': msg})

def login_view(request):
    form=LoginForm(request.POST or None)
    msg=None
    if request.method == 'POST' and form.is_valid():
        # cleaned_data , a dictionary which contains cleaned data only from the fields which have passed the validation tests.
        #  Note that cleaned_data attribute will only be available to you after you have invoked the is_valid() method
        username=form.cleaned_data['username']
        password=form.cleaned_data['password']
        # to authenticate
        user=authenticate(username=username,password=password)
        if user is not None and user.is_admin:
            login(request,user)
            return redirect('adminPage')
        elif user is not None and user.is_customer:
            login(request,user)
            return redirect('customer')
        elif user is not None and user.is_driver:
            login(request,user)
            return redirect('driver')
        else:
            msg='invalid credentials'
    else:
        msg='error validating form'
    return render(request, 'login.html',{'form':form,'msg':msg})

def admin(request):
    return render(request,'admin.html')

def customer(request):
    return render(request,'customer.html')

def driver(request):
    return render(request,'driver.html')   