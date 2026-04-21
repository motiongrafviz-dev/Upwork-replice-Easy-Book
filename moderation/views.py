from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.conf import settings

from .models import *
import json



name_of_client = ""
counte = 0
check = ""
user = ""
username_2 = ""
work_count = 1
global_amount = 0
save_data = {}
freelancer_data_chat = []
customers_data_chat = []
sorted_clients = {}
python = []
css = []
django = []
html = []
role = ""
changing_number = 0
roles = ""
new_role = ''
freelancers = []
# information for customers
reputation = "Normal"
ava = []
usernames = []
salary = 0
portfoli_projects = {}
skill_list = []

card = {
     
    
    
}





def main(request):
    return render(request, "moderation/staff_login.html", {})



def staff_login(request):
    global check,new_role
    b1 = (request.POST.get('b1') or '').strip()
    b2 = (request.POST.get('b2') or '').strip()
    if b1 == "b_1":
        check = "admin"
    elif b2 == "b_2":
        check = "moderator"
    print(check)
    return render(request, "moderation/staff_login.html")



def moving_to_staff_admin_pannel(request): 
    global check,skill_list,username_2, portfoli_projects,card,salary,usernames,role,new_role
    login_info = Login.objects.all()
    mod_requests = ModeratorAplication.objects.all()
    u_1 = (request.POST.get('username_poll') or '').strip()
    l_1 = (request.POST.get('login_poll') or '').strip()

    
    for i in login_info:
        if check == i.role and u_1 == i.username and l_1 == i.password and check == "admin":
            username_2 = i.username
            return render(request, "moderation/admin.html", {"username_2": username_2,"mod_requests": mod_requests})
        elif check == i.role and u_1 == i.username and l_1 == i.password and check == "moderator":
            support = Support.objects.all()
            
            username_2 = i.username
            return render(request, "moderation/moderator.html", {"username_2": username_2,"support": support, })
            

    return render(request, "moderation/index.html", {})


def delete_complain(request): 
    support = Support.objects.all()
    ide = (request.POST.get('complain_id') or '').strip()
    c = Support.objects.get(id=ide)  
    c.delete()

    return render(request, "moderation/moderator.html", {"support": support,})




def accept_complain(request): 
    support = Support.objects.all()
    ide = (request.POST.get('complain_id') or '').strip()
    id = Support.objects.get(id=ide)  
    id.accepted = "accepted"
    id.delete()
    id.save()
    return render(request, "moderation/moderator.html", {"support": support,"id":id})



def accept_application(request):
    global new_role
    moderator_application = ModeratorAplication.objects.all()
    ide = (request.POST.get('idq') or '').strip()
    id = ModeratorAplication.objects.get(id=ide)  
    new_role = id.name
    print(new_role)
    id.accepted_moder = "accepted"
    id.save()


    return render(request, "moderation/accepted_moderators.html", {"moderator_app": moderator_application})


def delete_application(request):
    moderator_applicatione = ModeratorAplication.objects.all()
    ide = (request.POST.get('ide') or '').strip()
    app = ModeratorAplication.objects.get(id=ide)
    app.delete()
    return render(request, "moderation/admin.html", {"mod_requests": moderator_applicatione})


def delete_moderator(request):
    moderator_applicatione = ModeratorAplication.objects.all()
    ide = (request.POST.get('ide') or '').strip()
    app = ModeratorAplication.objects.get(id=ide)
    app.accepted_moder = ""
    print(app.accepted_moder)
    app.save()
    print(app.accepted_moder)
    return render(request, "moderation/accepted_moderators.html", {"moderator_app": moderator_applicatione})

def block_client(request):
    saved_acc = Saved_acc.objects.all()
    client_id = (request.POST.get('client_id') or '').strip()
    app = Saved_acc.objects.get(id=client_id)
    app.delete()
    return render(request, "moderation/freelancer_admin_pannel.html", {"saved_acc": saved_acc})


def add_reputation(request):
    saved_acc = Saved_acc.objects.all()
    client_id = (request.POST.get('client_id') or '').strip()
    app = Saved_acc.objects.get(id=client_id)
    for i,v in app.acuonts.items():
        v["reputation"] = "High"

    app.save()
    print(app.acuonts)
    return render(request, "moderation/freelancer_admin_pannel.html", {"saved_acc": saved_acc})


def punish_freelancer(request):
    saved_acc = Saved_acc.objects.all()
    return render(request, "moderation/punish_payment.html", {"saved_acc": saved_acc})

def mines_money(request):
    investemoney = InvestedMoney.objects.all()
    punish = (request.POST.get('punish') or '').strip()
    int_punish = int(punish)
    for i in investemoney:
        print(i.money_invested)
        i.money_invested -= int_punish
        print(i.money_invested)
        i.save(update_fields=['money_invested'])
    return render(request, "moderation/punish_payment.html", {"punish": punish,})

def admin_panel_request_for_moderator(request):
    moderator_applicatione = ModeratorAplication.objects.all()
    return render(request, "moderation/admin.html", {"mod_requests": moderator_applicatione})

def admin_panel_request_for_accepted_moderators(request):
    moderator_applicatione = ModeratorAplication.objects.all()
    return render(request, "moderation/accepted_moderators.html", {"moderator_app": moderator_applicatione})

def admin_panel_request_for_freelancer(request):
    saved_acc = Saved_acc.objects.all()
    for i in saved_acc:
        for i,v in i.acuonts.items():
            print(i)
    return render(request, "moderation/freelancer_admin_pannel.html", {"saved_acc": saved_acc})\
    
def chat_with_offender(request): 
    global name_of_client
    support = Support.objects.all()
    for i in support:
        if name_of_client == i.complain_about_who:
            return redirect('enter_chat_2')
    return render(request, "moderation/moderator.html", {"support": support})

