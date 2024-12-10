from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from DetailsApp.models import StudentDatabase
from django.contrib.auth import authenticate, login, logout


# Create your views here.

@login_required(login_url='login')
def index(request):
    return render(request,'index.html')

def signin(request):
    b=''
    if request.method == 'POST':
        uname = request.POST.get('Uname')
        passwd = request.POST.get('Pwd')
        user = authenticate(request,username=uname,password=passwd)
        if user is not None:
            login(request,user)            
            return redirect('Home')
        else:
            b='Incorrect password or user does not exist'
    return render(request,'login.html',{'b':b})

def signup(request):
    a=''
    b=''
    if request.method == 'POST':
       uname = request.POST.get('Uname')
       uid = request.POST.get('Uid')
       pass1 = request.POST.get('pwd1')
       pass2 = request.POST.get('pwd2')
       if pass1 != pass2:
        a='Password does not matches'
        
       else:

        My_user = User.objects.create_user(uname,uid,pass1)
        My_user.save()
        return redirect("login")
        a ={'uname':n}
    return render(request,'signup.html',{'user':a})


def Data(request):
     if request.method =='POST':
        clas      =   request.POST.get('TITLE')
        Sub       =   request.POST.get('TALUK')
        Sem       =   request.POST.get('MONTH')
        att       =   request.POST.get('MONTH')
        
        name        =   request.POST.get('YEAR')
        usn         =   request.POST.get('ACC')
        save        =   StudentDatabase(NAME=name ,USN=usn ,CLASS=clas,SUB=Sub,SEM=Sem,ATT=att)
        save.save()
        D='Data Saved Scuessfully'
     else:
        P='Please Fill The Form'
   
     return HttpResponse("Saved Sucessfull")

def log_out(request):
    logout(request)
    return redirect('login')


