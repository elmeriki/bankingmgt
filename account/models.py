from django.db import models

class customer(models.Model):
    first_names = models.CharField(max_length=200)
    last_names = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.IntegerField()
    address = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    
class accountinfo(models.Model):
    customer = models.ForeignKey(customer, on_delete=models.CASCADE)
    accountno = models.IntegerField()
    accountype = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    
class accountbalance(models.Model):
    customer = models.ForeignKey(customer, on_delete=models.CASCADE)
    balance = models.IntegerField()
    
class statement(models.Model):
    customer = models.ForeignKey(customer, on_delete=models.CASCADE)
    transactiontype = models.CharField(max_length=200)
    amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    