from django.shortcuts import *
from .forms import *
from .models import *
from django.http import *
import hashlib
import datetime
from datetime import date
from django.contrib import messages
from django.core.mail import send_mail,EmailMessage
from django.conf import settings

# Create your views here.
def default(request):
    FormSignup1=FormSignup()
    FormLogin1=FormLogin()
    return render(request,"validation.html",{'FormLogin1':FormLogin1,'FormSignup1':FormSignup1})

def logincheck(request):
    # FormSignup1=FormSignup()
    # FormLogin1=FormLogin()
    formlog = FormLogin(request.POST, request.FILES)
    if formlog.is_valid():
        username=formlog.cleaned_data['user_name']
        password=formlog.cleaned_data['password']
        encpassword=hashlib.md5(password.encode())
        hashpassword=encpassword.hexdigest()
        try:
            getuserdata=Tbluser.objects.get(username=username)
            if getuserdata.passwordenc==hashpassword:
                request.session['username']=formlog.cleaned_data['user_name']
                request.session['getFirstandLastName']=getuserdata.firstname + " " + getuserdata.lastname
                messages.success(request,'login succesfull')
                return redirect('/index')
            else:
                messages.error(request,'Password Incorrect')
                return redirect('/')
        except:
            messages.error(request,'Username does not exisit')
            return redirect('/')

def signincheck(request):
    
    if request.method == "POST":
        
        formsignin = FormSignup(request.POST,request.FILES)
        
        if formsignin.is_valid():
            
            Password=formsignin.cleaned_data['password']
            ConfirmPassword=formsignin.cleaned_data['confirm_password']
            temp_username=formsignin.cleaned_data['username']
            if Password != ConfirmPassword:
                # return HttpResponse("Password not match 3")
                messages.error(request,'Password miss match')
                return redirect('/')

            else:
                # return HttpResponse("Password not match 4")
                try:
                    user = Tbluser.objects.get(username=temp_username)
                    if user.username==temp_username:
                        # return HttpResponse("Password not match 4")
                        messages.error(request,'Username not available. Try another one.')
                        return redirect('/')

                except:
                    # return HttpResponse("Password not match 4")
                    TbluserVar=Tbluser()
                    TbluserVar.firstname=formsignin.cleaned_data['firstname']
                    TbluserVar.lastname=formsignin.cleaned_data['lastname']
                    TbluserVar.username=formsignin.cleaned_data['username']
                    TbluserVar.mobilenumber=formsignin.cleaned_data['mobilenumber']
                    TbluserVar.dateofjoining=date.today()
                    TbluserVar.emailid=formsignin.cleaned_data['email']
                    TbluserVar.userlevel=0
                    PasswordEnc=hashlib.md5(Password.encode())
                    RealPassword=PasswordEnc.hexdigest()
                    TbluserVar.passwordenc=RealPassword
                    # TbluserVar.save()
                    request.session['username']=TbluserVar.username
                    request.session['getFirstandLastName']=TbluserVar.firstname + " " + TbluserVar.lastname
                    FullName=request.session['getFirstandLastName']
                    from_email=settings.EMAIL_HOST_USER
                    recipient_list=[formsignin.cleaned_data['email'],]
                    subject='Welcome to The Transponster.'
                    message='Successfully Logged in! Your Username is',temp_username
                    mail=EmailMessage(subject,message,from_email,recipient_list)
                    mail.send()
                    # mail=EmailMessage(subject,message,senter,recipient_list)
                    # mail.send()
                    TbluserVar.save()
                    return redirect('/index')

        else:
            
            return redirect('/')
    else:
        return HttpResponse("NOT CORRECT")

def index(request):
    try:
        username=request.session['username']
        FullName=request.session['getFirstandLastName']
        return render(request,"index.html",{'FullName':FullName})
    except:
        return HttpResponse("NOT CORRECT")
    

def search(request):
    FormSearchMovies1=FormSearchMovies()
    return render(request,"search.html",{'FormSearchMovies1':FormSearchMovies1})
