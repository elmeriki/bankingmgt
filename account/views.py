from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib.auth.models import User,auth
from django.contrib import  messages
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives
from account .models import *
import random

@login_required(login_url='/')
def createuserbankaccount(request):
    if request.user.is_superuser:
        return render(request,'createbankaccount.html')
    

@login_required(login_url='/')
def createdepositmethod(request):
    if request.user.is_superuser and request.method == "POST":
        customerid = request.POST['customerid']
        depositedamount = request.POST['amount']
        curentcustomer = accountbalance.objects.get(id=customerid)
        curentcustomer.balance =depositedamount
        curentcustomer.save()
        messages.info(request,'Account has been deposited successful')
        return render(request,'createdeposit.html')

@login_required(login_url='/')
def createdeposit(request):
    if request.user.is_superuser:
        return render(request,'createdeposit.html')

@login_required(login_url='/')
def createuseraccountinfo(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        if User.objects.filter(username=username).exists():
            messages.info(request,'Username is taken')
            return redirect('createuserbankaccount') 
        elif User.objects.filter(email=email):
            messages.info(request,'Email Address is taken')
            return redirect('createuserbankaccount')
        else:
            # saving data into user model to perform login actions
            firtsname = request.POST['firtsname']
            lastnames = request.POST['lastnames']
            accountype = request.POST['accountype']
            cellphonenumber = request.POST['cellphonenumber']
            paddress = request.POST['paddress']
            email = request.POST['email']
            username = request.POST['username']
            defaulpasssword = request.POST['password']
            userloginaccount = User.objects.create_user(username=username,first_name=firtsname,last_name=lastnames,password=defaulpasssword,email=email)
            userloginaccount.save()
            
            # saving data into customer model
            customerinfo = customer(first_names=firtsname,last_names=lastnames,email=email,phone=cellphonenumber,address=paddress)
            customerinfo.save()
            randomNumber = random.randint(1964600, 10083690)

            # saving data into acount model
            useraccountinfo = accountinfo(customer=customerinfo,accountno=randomNumber,accountype=accountype)
            useraccountinfo.save()
            
            # saving data into accountbalance model
            useraccountbalance = accountbalance(customer=customerinfo,balance=00)
            useraccountbalance.save()
            
            userstatement = statement(customer=customerinfo,transactiontype="None",amount=00)
            userstatement.save()
            messages.success(request,"User bank account has been created successfully")
            return redirect('createuserbankaccount') 

@login_required(login_url='/')       
def fetchbalance(request):
    if request.user.is_authenticated:
        current_user = request.user
        curent_user_email = current_user.email
        customerid = customer.objects.filter(email=curent_user_email)
        for userid in customerid:
            customerbalance = accountbalance.objects.filter(customer=userid.id)
            return render(request,'userbalance.html',{'customerbalance':customerbalance})
        
        

@login_required(login_url='/')       
def fetchstatement(request):
    if request.user.is_authenticated:
        current_user = request.user
        curent_user_id = current_user.id 
        customerstatement = statement.objects.filter(customer=curent_user_id)
        return render(request,'userstatement.html',{'customerstatement':customerstatement})
        
@login_required(login_url='/')       
def fetchuser(request):
    if request.user.is_authenticated:
        current_user = request.user
        curent_user_email = current_user.email
        userdata = customer.objects.filter(email=curent_user_email)
        return render(request,'usersettings.html',{'userdata':userdata})       
        
@login_required(login_url='/')   
def transfer(request):
    return render(request,'transfer.html')

        
@login_required(login_url='/') 
def transfermethod(request):
    if request.user.is_authenticated:
        current_user = request.user
        curent_user_email = current_user.email  
        curentcustomer = customer.objects.filter(email=curent_user_email)
        for custdata in curentcustomer:
            curentbalance = accountbalance.objects.filter(customer=custdata.id)
            for baldata in curentbalance:
                curentbalance = int(baldata.balance)
                if request.method == "POST":
                    amount = int(request.POST['amount'])
                    reference = request.POST['reference']
                    newbalance = curentbalance - amount
                    newbalanceupdate = accountbalance.objects.get(id=custdata.id)
                    newbalanceupdate.balance = newbalance
                    newbalanceupdate.save()
                    messages.success(request,"Transfer OK")
                    return render(request,'transfer.html')
                                
