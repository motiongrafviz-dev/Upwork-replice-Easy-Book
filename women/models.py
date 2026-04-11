from django.db import models
from django.urls import reverse





class Login(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
    acceptde_role = models.CharField(max_length=50)
    def __str__(self):
        return self.username

class Tags(models.Model):
    tags = models.CharField(max_length=100)
    def __str__(self):
        return self.tags

class Saved_acc(models.Model):
    acuonts = models.JSONField(default=dict)  
    def __str__(self):
        return str(self.acuonts)



class InvestedMoney(models.Model):
    money = models.IntegerField()  
    money_invested = models.IntegerField()  
    card_number = models.IntegerField() 
def __str__(self):
    return f"{self.card_number} — {self.money}$ = {self.money_invested}"




class Chat(models.Model):
    message = models.CharField(max_length=100)
    user = models.CharField(max_length=10)
    messages = models.JSONField(default=dict)

    def __str__(self):
        return f"{self.user}: {self.message}"

    
    
class SaveMesages(models.Model):
    messages_freelancer = models.JSONField(default=list)
    messages_client = models.JSONField(default=list)
    
    def __str__(self):
        return f"{self.messages_freelancer}: {self.messages_client}"
    
    

class Photo(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='photos/') 
    
    
    
class Reviews(models.Model):
    freelancer = models.CharField(max_length=100)  
    user = models.CharField(max_length=10)
    messages = models.CharField(max_length=100)
    stars = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.user}: {self.messages}"
    

class PaymentSystem(models.Model):
    freelancer_name = models.CharField(max_length=100)
    clients = models.IntegerField() 
    freelancers = models.IntegerField() 
    

class Support(models.Model):
    text_of_complain = models.CharField(max_length=250)
    who_writing = models.CharField(max_length=50)
    accepted = models.CharField(max_length=50)
    complain_about_who = models.CharField(max_length=50) 


class ModeratorAplication(models.Model):
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    accepted_moder = models.CharField(max_length=50)
    check_moderator = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    reason = models.CharField(max_length=100) 
    process = models.CharField(max_length=100) 
    violation = models.CharField(max_length=100) 