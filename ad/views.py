from django.shortcuts import render,redirect
from .models import Employee
from .models import User
import re
from django.contrib.auth.hashers import make_password,check_password
# Create your views here.
def index(request):
    emp=Employee.get_all_products
    return render(request,'rr.html',{'emp':emp})
def login(request):
    if request.method =='GET':
        return render(request,'login.html')
    else:
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=User.get_email_id(email)
        error_message=None
        if(user):
            flag=check_password(password,user.password)
            if flag:
                request.session['user']=user.id

                redirect('home')
            else:
                error_message="wrong password"
        else:
            error_message="email invalid"
        return render(request,'login.html',{'error':error_message})



def signup(request):
    if request.method =='GET':
        return render(request,'signup.html')
    else:
        first_name=request.POST.get('first_name')
        email=request.POST.get('email')
        password=request.POST.get('password')

        user = User(first_name=first_name, email=email, password=password)

        #validation
        error_message=None
        if(len(first_name)<4):
            error_message="First Name must be 4 char long!"
        if not re.match(r"^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$", email):
            error_message = "Email should be valid!"

        SpecialSym = ['$', '@', '#', '%']
        val = True

        if len(password) < 8:
            error_message="password should be 8 char"
        elif user.userExits():
            error_message="useralready exists"



#saving
        if(not error_message):
            user.password=make_password(user.password)
            user.register()
            return redirect('login')
        else:
            return render(request,'signup.html',{'error':error_message})


def logout(request):
    request.session.clear()
    return redirect('login')