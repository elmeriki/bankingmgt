from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib.auth.models import User,auth
from django.contrib import  messages
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives
from account .models import *

# Create your views here.
def login(request):
    return render(request,"login.html")

#user logingout functionality
def logout(request):
    auth.logout(request)
    messages.info(request,"Logout Successfully")
    return redirect('/')

@login_required(login_url='/')
def dashboard(request):
    # checking is a user is authenticated
    if request.user.is_authenticated:
        current_user = request.user
        # fetching the curent login user to compare with the curent login
        curent_user_email = current_user.email
        
        # fetcing the data base on the login user
        customerdata = customer.objects.filter(email=curent_user_email)
        for data in customerdata:
            data = {
            "first_names":data.first_names,
            "last_names":data.last_names,
            "address":data.address,
            "email":data.email,
            "phone":data.phone,
            "dataopen":data.created_at
            }
        return render(request,'userprofile.html',context=data)
        
@login_required(login_url='/')      
def accountdata(request):
    if request.user.is_authenticated:
        current_user = request.user
        curent_user_id = current_user.id
        useraccountinfo = accountinfo.objects.filter(customer=curent_user_id)
        for data in useraccountinfo:
                accountdata = {
            "accountno":data.accountno,
            "accounttype":data.accountype
        }
        return render(request,'userprofile.html',context=accountdata)
            

def userlogin(request):
    # User login registration
    if request.method=='POST':
        username = request.POST['username'] 
        password = request.POST['password']   
        userlog = auth.authenticate(username=username, password=password)
        # checking if it is an existing user in the database
        
        # customise error messages handler
        if userlog is not None:
            auth.login(request, userlog)
            return redirect('dashboard')
            # making redirect if it is successful
        else:
            messages.info(request,"Bad Login Details")
            return redirect('/')      
            # sending an error message if not succesfully login 
            
# def register(request):
    
#     if request.method == 'POST':
#         # collecting data from the form and storing in tem variables
#         uname = request.POST['username']
#         useremail = request.POST['email']
#         passcode = request.POST['password']
#         if User.objects.filter(username=uname).exists():
#             messages.info(request,'Username is taken')
#             return redirect('createaccount') 
#         elif User.objects.filter(email=useremail):
#             messages.info(request,'Email Address is taken')
#             return redirect('createaccount')
        
#         else:
#             registerUser = User.objects.create_user(username=uname,password=passcode,email=useremail)
#             registerUser.save()
#             messages.success(request,"Account created successfully Email in progess")
#             subject = 'Sign-Up Confirmation'
#             from_email = 'elmeriki@gmail.com'
#             to = useremail
#             text_content = 'This is an important message.'
#             html_content = '<p>This is an <strong>important</strong> message.</p>'
#             msg = EmailMultiAlternatives(subject, text_content, from_email,[to])
#             msg.attach_alternative(html_content, "text/html")
#             msg.send()
#             messages.success(request,"Confirmation email sent")
#             return redirect('createaccount') 
    