from django.db import models
from django.urls import reverse



class ModeratorAplication(models.Model):
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    accepted_moder = models.CharField(max_length=50)
    check_moderator = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    reason = models.CharField(max_length=100) 
    process = models.CharField(max_length=100) 
    violation = models.CharField(max_length=100) 

class Login(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
    acceptde_role = models.CharField(max_length=50)
    def __str__(self):
        return self.username

class Support(models.Model):
    text_of_complain = models.CharField(max_length=250)
    who_writing = models.CharField(max_length=50)
    accepted = models.CharField(max_length=50)
    complain_about_who = models.CharField(max_length=50) 


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
