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
    return render(request, "clients_freelancers/register.html", {})

def login(request):
    return render(request, "clients_freelancers/login.html", {})





def searching_for_freelancers(request):
    login_info = Login.objects.all()
    acount_info = Saved_acc.objects.all()
    support = Support.objects.all()
    money = InvestedMoney.objects.all()
    payment = PaymentSystem.objects.all()
    moderator_application = ModeratorAplication.objects.all()
    for ie in money:
        return render(request, "clients_freelancers/search_for_freelancers.html", {"acount_info": acount_info, "amount_of_money": ie.money_invested,
        "MEDIA_URL": settings.MEDIA_URL, "payment": payment,"username_2": username_2,
            "freelancers":freelancers,
            "login_info":login_info,})


def checks_who_are_you(request):
    global check
    b1 = (request.POST.get('b1') or '').strip()
    b2 = (request.POST.get('b2') or '').strip()
    if b1 == "b_1":
        check = "customer"
    elif b2 == "b_2":
        check = "freelancer"
    print(check)
    
    return render(request, 'clients_freelancers/login.html',)

def moving_you_to_window(request): 
    global check,skill_list,username_2, portfoli_projects,card,salary,usernames,role
    login_info = Login.objects.all()
    acount_info = Saved_acc.objects.all()
    support = Support.objects.all()
    money = InvestedMoney.objects.all()
    payment = PaymentSystem.objects.all()
    moderator_application = ModeratorAplication.objects.all()
    amount_of_money = 0
    paied_freelancer = {}
    u_1 = (request.POST.get('username_poll') or '').strip()
    l_1 = (request.POST.get('login_poll') or '').strip()

    for i in login_info:
        if check == "customer" and u_1 == i.username and l_1 == i.password and check == i.role:
            username_2 = i.username
            user = Login.objects.get(username=u_1)
            if user.role == "moderator":
                user.acceptde_role = "your application got accepted"
                user.save(update_fields=['acceptde_role'])

            for iq in payment:
                if iq.client_name == username_2:
                    for ie in acount_info:
                        for i,v in ie.acuonts.items():
                            if i == iq.freelancer_name:
                                paied_freelancer = v
            try:
                user_name = ModeratorAplication.objects.get(name=username_2)
            except ModeratorAplication.DoesNotExist:
                user_name = None
            print(paied_freelancer)

            for ie in money:
                amount_of_money = ie.money_invested
            return render(request, "clients_freelancers/customer.html", {"acount_info": acount_info, "amount_of_money": amount_of_money,
            "MEDIA_URL": settings.MEDIA_URL, "payment": payment,"username_2": username_2,
            "freelancers":freelancers,
            "login_info":login_info, "user_name": user_name, "paied_freelancer":paied_freelancer})
        if check == "freelancer" and u_1 == i.username and l_1 == i.password and check == i.role:
            username_2 = i.username
            usernames.append(i.username)
            chat = Chat.objects.all()
            return render(request, "clients_freelancers/freelancer.html", {"username_2": username_2, "acount_info": acount_info, "message": "brrrr", "MEDIA_URL": settings.MEDIA_URL, "support": support})
            

           

    return render(request, "clients_freelancers/index.html")




def redectar_freelancer(request): 
    global username_2
    acount_info = Saved_acc.objects.all()
    support = Support.objects.all()


    return render(request, "women/redectar_freelancer.html", {"username_2": username_2, "acount_info": acount_info, "message": "brrrr", "MEDIA_URL": settings.MEDIA_URL, "support": support})






def delete_msg_about_accepting_complain(request):
    global username_2
    support_for_accepting = Support.objects.filter(who_writing=username_2).all()
    support = Support.objects.all()
    acount_info = Saved_acc.objects.all()
    for i in support_for_accepting:
        i.accepted = ""
        i.save(update_fields=['accepted'])
    return render(request, "clients_freelancers/redectar_freelancer.html", {"skill_list": skill_list, "username_2": username_2, "acount_info": acount_info, "message": "brrrr", "MEDIA_URL": settings.MEDIA_URL, "support": support})



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
    return render(request, 'clients_freelancers/redectar_freelancer.html', {"skill_list": skill_list, "username_2": username_2, "acount_info": acount_info, "message": "brrrr", "MEDIA_URL": settings.MEDIA_URL,})



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


    return render(request, 'clients_freelancers/redectar_freelancer.html', {"skill_list": skill_list, "username_2": username_2, "acount_info": acount_info, "message": "brrrr", "MEDIA_URL": settings.MEDIA_URL,})


def portfolio(request):
    return render(request, "clients_freelancers/portfolio.html", {})

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
        return render(request, "clients_freelancers/portfolio.html", {})

    else:
        print("sorry we already have this title")

 
    return render(request, "clients_freelancers/add_page.html", {})



def project_1(request):
    global portfoli_projects

    portfoli_projects_list_1 = list(portfoli_projects.keys())[0]
    print(portfoli_projects)

    
    return render(request, "clients_freelancers/project_1.html", {"title": portfoli_projects_list_1, "value": portfoli_projects[portfoli_projects_list_1]})
    

def project_2(request):
    global portfoli_projects
    try:
        portfoli_projects_list_2 = list(portfoli_projects.keys())[1]
    except IndexError:
        return render(request, "clients_freelancers/project_2.html", {"message": "before coming to this tamplate fill it"})
    print(portfoli_projects)
    return render(request, "clients_freelancers/project_1.html", {"title": portfoli_projects_list_2, "value": portfoli_projects[portfoli_projects_list_2]})



def acc_apply(request):
    global card,username_2,portfoli_projects,skill_list,usernames,ava
    obj = Saved_acc.objects.first()
    data = obj.acuonts
    data[username_2] = card[username_2]
    obj.save()
    del card[username_2]
    skill_list = []
    portfoli_projects = {}
    username_2 = ""
    ava = ""
    usernames = []
    print(card)
    print(data)
    return render(request, "clients_freelancers/index.html")
    
    
    
def invest_money(request):
    money = InvestedMoney.objects.all()
    amount = (request.POST.get('amount') or '').strip()
    card_number = (request.POST.get('card_number') or '').strip()
    if amount and card_number:
        amount = int(amount)
        card_number = int(card_number)
        for i in money:
            print(i.money, amount)
            print(i.card_number, card_number)
            if amount > i.money:
                return render(request, "clients_freelancers/customer.html", {"message": "you don,t have enough money"})
            elif card_number != i.card_number:
                return render(request, "clients_freelancers/customer.html", {"message": "card number is wrong"})
            if i.card_number == card_number and amount <= i.money:
                i.money -= amount
                i.save(update_fields=['money'])
                i.money_invested = amount
                i.save(update_fields=['money_invested'])
                login_info = Login.objects.all()
                acount_info = Saved_acc.objects.all()
                support = Support.objects.all()
                money = InvestedMoney.objects.all()
                payment = PaymentSystem.objects.all()
                moderator_application = ModeratorAplication.objects.all()
                for ie in money:
                    try:
                        user_name = ModeratorAplication.objects.get(name=username_2)
                    except ModeratorAplication.DoesNotExist:
                        user_name = None
                    return render(request, "clients_freelancers/search_for_freelancers.html", {"acount_info": acount_info, "amount_of_money": ie.money_invested,
                    "MEDIA_URL": settings.MEDIA_URL, "payment": payment,"username_2": username_2,
                        "freelancers":freelancers,
                        "login_info":login_info, "user_name": user_name})

    return render(request, "clients_freelancers/add_money.html")
    
    


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
    return render(request, "clients_freelancers/portfolio.html")
    


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
                    return render(request, "clients_freelancers/profiles.html", {"data": save_data, "message": "you don,t have enough money to hire him", "photos": photo, "acount_info": data, "payment": payment})
                else:
                    i.money_invested -= int(pricee) 
                    i.save(update_fields=['money_invested'])
                    for ie in chat:
                        ie.message = "hired"
                        ie.user = user
                        ie.save(update_fields=['message', 'user'])  
                    return render(request, "clients_freelancers/profiles.html", {"data": save_data, "photos": photo, "acount_info": data, "chat": chat, "reviews": reviews, "payment": payment})
                
    return render(request, "clients_freelancers/profiles.html", {"data": save_data, "photos": photo, "acount_info": data, "chat": chat, "reviews": reviews})


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
        return render(request, "clients_freelancers/chat_customer.html", {"messages_client": chat, "freelancer_name": name_of_freelancer})



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
    return render(request, "clients_freelancers/chat.html", {"messages_from_freelancer": chat, "client_name": name_of_client})




    
def chat_freelancer(request):
    global username_2,freelancer_data_chat,user
    chat = Chat.objects.all()
    support = Support.objects.all()

    messages = (request.POST.get("message") or '').strip()
    freelancer_data_chat.append(messages)

    for ie in chat:
        ie.messages[username_2] = freelancer_data_chat
        ie.save(update_fields=['messages'])
        if "support" in freelancer_data_chat:
            from_user = (request.POST.get("from_user") or '').strip()
            to_user = (request.POST.get("to_user") or '').strip()
            report_text = (request.POST.get("report_text") or '').strip()
            print(from_user, to_user,report_text)
            Support.objects.create(text_of_complain=report_text, who_writing=from_user,complain_about_who=to_user)
            return render(request, "clients_freelancers/support.html", {"support": support})
        return render(request, "clients_freelancers/chat.html", {"messages_from_freelancer": chat, "freelancer_name": username_2})
    return render(request, "clients_freelancers/chat.html",{"messages_from_freelancer": chat, "freelancer_name": username_2})



def save_messages(request):
    global freelancer_data_chat
    chat = Chat.objects.all()
    saved_messages = SaveMesages.objects.all()

    for ie in saved_messages:
        ie.messages_freelancer = freelancer_data_chat
        ie.save(update_fields=['messages_freelancer'])
        print(ie.messages_freelancer)
    return render(request, "clients_freelancers/portfolio.html")







    
def chat_customer(request):
    global username_2,customers_data_chat
    chat = Chat.objects.all()
    messages = (request.POST.get("message") or '').strip()
    customers_data_chat.append(messages)

    for ie in chat:
        ie.messages[username_2] = customers_data_chat
        ie.save(update_fields=['messages'])
        print(user)
        for i in customers_data_chat:
            print(i)
            if "Pay" in i:
                customers_data_chat.remove("Pay")
                acount_info = Saved_acc.objects.all()
                for i in acount_info:
                    for name,data in i.acuonts.items():
                        return render(request, "women/payment.html", {"acount_info": data})
        return render(request, "clients_freelancers/chat_customer.html", {"messages_client": chat, "client_name": username_2})
    
    return render(request, "clients_freelancers/chat_customer.html",{"messages_client": chat, "client_name": username_2})



def save_messages_2(request):
    global customers_data_chat
    chat = Chat.objects.all()
    saved_messages = SaveMesages.objects.all()

    for ie in saved_messages:
        ie.messages_client = customers_data_chat
        ie.save(update_fields=['messages_client'])
        print(ie.messages_client)
    return render(request, "clients_freelancers/portfolio.html")
    
    
    
def check_tags(request):
    global sorted_clients
    saved_acc = Saved_acc.objects.all()
    for i in saved_acc:
        for name, data in i.acuonts.items():
            sorted_clients[data["username_org"][0]] = data["tags"]
    print(sorted_clients)
    login_info = Login.objects.all()
    acount_info = Saved_acc.objects.all()
    support = Support.objects.all()
    money = InvestedMoney.objects.all()
    payment = PaymentSystem.objects.all()
    moderator_application = ModeratorAplication.objects.all()
    for ie in money:
        try:
            user_name = ModeratorAplication.objects.get(name=username_2)
        except ModeratorAplication.DoesNotExist:
            user_name = None
        return render(request, "clients_freelancers/search_for_freelancers.html", {"acount_info": acount_info, "amount_of_money": ie.money_invested,
        "MEDIA_URL": settings.MEDIA_URL, "payment": payment,"username_2": username_2,
            "freelancers":freelancers,
            "login_info":login_info, "user_name": user_name})

     
def sort_by_tags(request):
    global sorted_clients, python, css, django, html
    saved_acc = Saved_acc.objects.all()
    for i in saved_acc:
        for name, data in i.acuonts.items():
            print(data["username_org"])
            if data.get("username_org"): 
                sorted_clients[data["username_org"][0]] = data["tags"]
                print(sorted_clients)

                
    for i,v in sorted_clients.items():
        if "Python" in v:
            python.append(i)
        if "HTML" in v:
            html.append(i)
        if "CSS" in v:
            css.append(i)
        if "Django" in v:
            django.append(i)
            
    
    print(python, css, django,html)
    login_info = Login.objects.all()
    acount_info = Saved_acc.objects.all()
    support = Support.objects.all()
    money = InvestedMoney.objects.all()
    payment = PaymentSystem.objects.all()
    moderator_application = ModeratorAplication.objects.all()
    for ie in money:
        try:
            user_name = ModeratorAplication.objects.get(name=username_2)
        except ModeratorAplication.DoesNotExist:
            user_name = None
        return render(request, "clients_freelancers/search_for_freelancers.html", {"acount_info": acount_info, "amount_of_money": ie.money_invested,
        "MEDIA_URL": settings.MEDIA_URL, "payment": payment,"username_2": username_2,
            "freelancers":freelancers,
            "login_info":login_info, "user_name": user_name})
    
def htmle(request):
    global html
    result = []
    saved_acc = Saved_acc.objects.all()
    for i in saved_acc:
        for ie,v in i.acuonts.items():
            if ie in html:
                print(ie,v)
                result.append(v)
    return render(request, "clients_freelancers/html.html", {"else": result})


def pythone(request):
    global python
    result = []
    saved_acc = Saved_acc.objects.all()
    for i in saved_acc:
        for ie,v in i.acuonts.items():
            if ie in python:
                print(ie,v)
                result.append(v)
    print(result)
    return render(request, "clients_freelancers/python.html", {"else": result})
def djangoe(request):
    global django
    result = []
    saved_acc = Saved_acc.objects.all()
    for i in saved_acc:
        for ie,v in i.acuonts.items():
            if ie in django:
                print(ie,v)
                result.append(v)
    return render(request, "clients_freelancers/django.html", {"else": result})
def csse(request):
    global css
    result = []
    saved_acc = Saved_acc.objects.all()
    for i in saved_acc:
        for ie,v in i.acuonts.items():
            if ie in css:
                print(ie,v)
                result.append(v)
    return render(request, "clients_freelancers/css.html", {"else": result})



def select_role(request):
    global role,skill_list,username_2
    acount_info = Saved_acc.objects.all()
    support = Support.objects.all()
    role_1 = (request.POST.get("role") or '').strip()
    role = role_1
    print(role)
    return render(request, "clients_freelancers/redectar_freelancer.html", {"skill_list": skill_list, "username_2": username_2, "acount_info": acount_info, "message": "brrrr", "MEDIA_URL": settings.MEDIA_URL, "support": support,})    

def upload_photo(request):
    global ava
    photos = Photo.objects.all()
    photo_name = request.FILES.get("photoe")
    name_photo = request.POST.get("name_photo")
    ava.append(f"photos/{photo_name.name}")
    print(photo_name, name_photo)
    return render(request, "clients_freelancers/upload_photo.html", {'photos': photos})

def the_photo(request):
    global ava
    ava = []
    photos = Photo.objects.all()
    return render(request, "clients_freelancers/upload_photo.html", {"photos": photos})


def reviews_from_customers(request):
    return render(request, "clients_freelancers/reviews.html")


import ast
def see_profile(request):
    global save_data,user
    reviews = Reviews.objects.all()
    saved_acc = Saved_acc.objects.all()
    acount_info = Saved_acc.objects.all()
    chat = Chat.objects.all()
    photo = Photo.objects.all()
    payment = PaymentSystem.objects.all()
    name_of_freelanser = (request.POST.get("user") or '').strip()
    real_list = ast.literal_eval(name_of_freelanser)
    user = real_list[0]

    for ie in reviews:
        print(user, ie.freelancer)
    
    for i in acount_info:
        for name,data in i.acuonts.items():
            for i in saved_acc:
                for name, data in i.acuonts.items():
                    if real_list[0] in name:
                        save_data = data
                        return render(request, "clients_freelancers/profiles.html", {"data": data, "photos": photo, "acount_info": data, "chat": chat, "reviews": reviews, "usere": user, "for_who": ie.freelancer, "payment": payment})

    login_info = Login.objects.all()
    acount_info = Saved_acc.objects.all()
    support = Support.objects.all()
    money = InvestedMoney.objects.all()
    payment = PaymentSystem.objects.all()
    moderator_application = ModeratorAplication.objects.all()
    for ie in money:
        try:
            user_name = ModeratorAplication.objects.get(name=username_2)
        except ModeratorAplication.DoesNotExist:
            user_name = None
        return render(request, "clients_freelancers/search_for_freelancers.html", {"acount_info": acount_info, "amount_of_money": ie.money_invested,
        "MEDIA_URL": settings.MEDIA_URL, "payment": payment,"username_2": username_2,
            "freelancers":freelancers,
            "login_info":login_info, "user_name": user_name})



def write_reviews(request):
    global username_2
    reviews = Reviews.objects.all()
    for_who = request.POST.get("for_who")
    print(user, for_who)
    messages_1 = request.POST.get("message")
    for i in range(1,6):
        stars_1 = request.POST.get(f"stars{i}")
        if stars_1 and messages_1:
            Reviews.objects.create(freelancer=for_who,user=username_2, messages=messages_1,stars=stars_1)
                
    return render(request, "clients_freelancers/reviews.html", {"reviews": reviews, "usere": user, "for_who": for_who})




def paying_system(request):
    global changing_number
    acount_info = Saved_acc.objects.all()
    paymentsystem = PaymentSystem.objects.all()
    freelancer_name = request.POST.get("freelancer_name")
    card_number = request.POST.get("card_number")
    card_number = int(card_number)
    money = InvestedMoney.objects.all()
    for i in acount_info:
        for name,data in i.acuonts.items():
            for ie in money:
                if ie.card_number == card_number and data["username_org"][0] == freelancer_name:
                    changing_number = 1
                    for i in paymentsystem:
                        i.clients += changing_number
                        i.freelancers += changing_number
                        changing_number = 0
                        i.save(update_fields=['clients'])
                        i.save(update_fields=['freelancers'])
                else:
                    print("not nice")
        

            return render(request, "clients_freelancers/payment.html", {"acount_info": data})
    return render(request, "clients_freelancers/payment.html", {"acount_info": data})



