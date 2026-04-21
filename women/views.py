from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.conf import settings

from .forms import *
from .models import *
import json
# from .forms import NewPageForm

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

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1></h1>')

def main(request):
    money = InvestedMoney.objects.all()
    for i in money:
        i.save(update_fields=['money_invested'])
        return render(request, "women/index.html", {"amount_of_money": i.money_invested})
    return render(request, "women/index.html", {"amount_of_money": i.money_invested})

def login(request):
    return render(request, "women/login.html", {})

def register(request):
    return render(request, "women/register.html", {})

def checks_who_are_you(request):
    global check
    b1 = (request.POST.get('b1') or '').strip()
    b2 = (request.POST.get('b2') or '').strip()
    if b1 == "b_1":
        check = "customer"
    elif b2 == "b_2":
        check = "freelancer"
    print(check)
    
    return render(request, 'women/login.html',)

 




def check_role(request):
    global roles
    q_role_1 = (request.POST.get('freelancer') or '').strip()
    q_role_2 = (request.POST.get('client') or '').strip()
    if q_role_1 == "freelancer_":
        roles = "freelancer"
    elif q_role_2 == "client_":
        roles = "customer"
    print(roles)
    return render(request, "women/register.html")



def register_pole(request):
    global counte,username,roles
    login_info = Login.objects.all()

    q_1 = (request.POST.get('username') or '').strip()
    q_2 = (request.POST.get('password') or '').strip()
    age = (request.POST.get('age') or '').strip()

    for i in login_info:
        if i.password != q_2 and i.username != q_1 and q_1 and q_2:
            counte += 1
            print("GOOD")
            Login.objects.create(username=q_1, password=q_2,role=roles)
            return render(request, "women/index.html", {})

        elif age:
            if int(age) < 18:
                return render(request, "women/index.html", {})
    
        elif counte == 2:
            counte = 0
            return render(request, 'women/index.html', {'login_info': login_info})

        print(counte)
    return render(request, 'women/register.html')







def remove_tag(request):
    global skill_list,username_2,portfoli_projects,usernames,ava,reputation
    acount_info = Saved_acc.objects.all()
    tags_list = Tags.objects.all()
    input_delete = (request.GET.get('delete') or '').strip()
    print(skill_list)
    for i in tags_list:
        if input_delete in skill_list and input_delete in i.tags:
            skill_list.remove(input_delete)
            card[username_2] = {
            "tags": skill_list,
            "portfolio": portfoli_projects,
            "username_org": usernames,   
            "salary": salary,
            "role": role,
            "ava": ava,
            "reputation": reputation
                }
            
    print(card)
    return render(request, 'women/redectar_freelancer.html', {"skill_list": skill_list, "username_2": username_2, "acount_info": acount_info, "message": "brrrr", "MEDIA_URL": settings.MEDIA_URL,})



def add_tag(request):
    global skill_list,username_2,portfoli_projects,reputation
    acount_info = Saved_acc.objects.all()
    tags_list = Tags.objects.all()
    input_add = (request.GET.get('add') or '').strip()
    for i in tags_list:
        if input_add not in skill_list and input_add in i.tags:
            skill_list.append(input_add)
        else:
            print("sorry its not tag")

    input_add = ""
    card[username_2] = {
    "tags": skill_list,
    "portfolio": portfoli_projects,
    "username_org": usernames,   
    "salary": salary,
    "role": role,
    "ava": ava,
    "reputation": reputation,
        }
    print(card, role)


    return render(request, 'women/redectar_freelancer.html', {"skill_list": skill_list, "username_2": username_2, "acount_info": acount_info, "message": "brrrr", "MEDIA_URL": settings.MEDIA_URL,})


def portfolio(request):
    return render(request, "women/portfolio.html", {})

def add_page(request):
    global portfoli_projects,ava,reputation
    saved = ""
    title = (request.POST.get('title') or '').strip()
    code = (request.POST.get('code') or '').strip() 
    for i in portfoli_projects.keys():
        saved = i
    
    if title and code and title != saved:
        portfoli_projects[title] = code
        card[username_2] = {
        "tags": skill_list,
        "portfolio": portfoli_projects,
        "username_org": usernames,   
        "salary": salary,
        "role": role,
        "ava": ava,
        "reputation": reputation
            }
        print(card)
        print(saved)
        return render(request, "women/portfolio.html", {})

    else:
        print("sorry we already have this title")

 
    return render(request, "women/add_page.html", {})






def staff_login(request):
    global check,new_role
    b1 = (request.POST.get('b1') or '').strip()
    b2 = (request.POST.get('b2') or '').strip()
    if b1 == "b_1":
        check = "admin"
    elif b2 == "b_2":
        check = "moderator"
    print(check)
    return render(request, "women/staff_login.html")












def project_1(request):
    global portfoli_projects

    portfoli_projects_list_1 = list(portfoli_projects.keys())[0]
    print(portfoli_projects)

    
    return render(request, "women/project_1.html", {"title": portfoli_projects_list_1, "value": portfoli_projects[portfoli_projects_list_1]})
    

def project_2(request):
    global portfoli_projects
    try:
        portfoli_projects_list_2 = list(portfoli_projects.keys())[1]
    except IndexError:
        return render(request, "women/project_2.html", {"message": "before coming to this tamplate fill it"})
    print(portfoli_projects)
    return render(request, "women/project_1.html", {"title": portfoli_projects_list_2, "value": portfoli_projects[portfoli_projects_list_2]})




def acc_apply(request):
    global card,username_2,portfoli_projects,skill_list,usernames,ava
    Saved_acc.objects.create(acuonts=card)
    del card[username_2]
    skill_list = []
    portfoli_projects = {}
    username_2 = ""
    ava = ""
    usernames = []
    print(card)
    return render(request, "women/index.html")
    
    
    
    


def price_per_project(request):
    global card,salary,reputation
    salary_a = (request.GET.get('salary') or '').strip()
    salary = salary_a
    card[username_2] = {
    "tags": skill_list,
    "portfolio": portfoli_projects,
    "username_org": usernames,   
    "salary": salary,
    "role": role,
    "ava": ava,
    "reputation": reputation,
        }
    return render(request, "women/portfolio.html")
    


def hire_freelancer(request):
    global save_data,user
    reviews = Reviews.objects.all()
    chat = Chat.objects.all()
    payment = PaymentSystem.objects.all()
    money = InvestedMoney.objects.all()
    photo = Photo.objects.all()
    pricee = (request.POST.get("price") or '').strip()
    acount_info = Saved_acc.objects.all()
    for i in acount_info:
        for name,data in i.acuonts.items():
            for i in money:
                
                if i.money_invested < int(pricee):
                    return render(request, "women/profiles.html", {"data": save_data, "message": "you don,t have enough money to hire him", "photos": photo, "acount_info": data, "payment": payment})
                else:
                    i.money_invested -= int(pricee) 
                    i.save(update_fields=['money_invested'])
                    for ie in chat:
                        ie.message = "hired"
                        ie.user = user
                        ie.save(update_fields=['message', 'user'])  
                    return render(request, "women/profiles.html", {"data": save_data, "photos": photo, "acount_info": data, "chat": chat, "reviews": reviews, "payment": payment})
                
    return render(request, "women/profiles.html", {"data": save_data, "photos": photo, "acount_info": data, "chat": chat, "reviews": reviews})


def enter_chat_2(request):
    global customers_data_chat,username_2
    name_of_freelancer = ""
    saved_messages = SaveMesages.objects.all()
    chat = Chat.objects.all()
    for i in saved_messages:
        customers_data_chat = i.messages_client
        print(customers_data_chat)
        for ie in chat:
            for i,v in ie.messages.items():
                if username_2 != i and i:
                    name_of_freelancer = i
        return render(request, "women/chat_customer.html", {"messages_client": chat, "freelancer_name": name_of_freelancer})



def enter_chat(request):
    global username_2,user,name_of_client

    
    print(user)
    saved_messages = SaveMesages.objects.all()
    chat = Chat.objects.all()
    for i in saved_messages:
        freelancer_data_chat = i.messages_freelancer
    
    
    print(freelancer_data_chat)
    for ie in chat:
        for i,v in ie.messages.items():
            if username_2 != i and i:
                name_of_client = i

    if "support" in freelancer_data_chat:
        freelancer_data_chat.remove("support")
    return render(request, "women/chat.html", {"messages_from_freelancer": chat, "client_name": name_of_client})





def save_messages(request):
    global freelancer_data_chat
    chat = Chat.objects.all()
    saved_messages = SaveMesages.objects.all()

    for ie in saved_messages:
        ie.messages_freelancer = freelancer_data_chat
        ie.save(update_fields=['messages_freelancer'])
        print(ie.messages_freelancer)
    return render(request, "women/portfolio.html")







def moderator_application(request):
    name = (request.POST.get('name') or '').strip()
    age = (request.POST.get('age') or '').strip()
    experience = (request.POST.get('experience') or '').strip()
    reason = (request.POST.get('reason') or '').strip()
    process = (request.POST.get('process') or '').strip()
    violation = (request.POST.get('violation') or '').strip()



    ModeratorAplication.objects.create(name=name, age=age,experience=experience,reason=reason,process=process,violation=violation)


    return render(request, "women/application_for_moderator.html")









