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

 


def moving_you_to_window(request): 
    global check,skill_list,username_2, portfoli_projects,card,salary,usernames,role
    login_info = Login.objects.all()
    acount_info = Saved_acc.objects.all()
    support = Support.objects.all()
    money = InvestedMoney.objects.all()
    u_1 = (request.POST.get('username_poll') or '').strip()
    l_1 = (request.POST.get('login_poll') or '').strip()

    for i in login_info:

        if check == "customer" and u_1 == i.username and l_1 == i.password and check == i.role:
            
            username_2 = i.username
            print(username_2)
            for i in money:
                i.save(update_fields=['money_invested'])
                print(card)
                print()
                return render(request, "women/customer.html", {"acount_info": acount_info, "amount_of_money": i.money_invested, "MEDIA_URL": settings.MEDIA_URL})
        elif check == "freelancer" and u_1 == i.username and l_1 == i.password and check == i.role:
            username_2 = i.username
            print(username_2)
            usernames.append(i.username)
            chat = Chat.objects.all()
            for i in chat:
                if i.message and i.user == username_2:
                    print("e", i.user, username_2, i.message)
                    return render(request, "women/freelancer.html", {"username_2": username_2, "acount_info": acount_info, "message": "brrrr", "MEDIA_URL": settings.MEDIA_URL, "support": support})
            

           

    return render(request, "women/index.html")





def delete_msg_about_accepting_complain(request):
    global username_2
    support_for_accepting = Support.objects.filter(who_writing=username_2).all()
    support = Support.objects.all()
    acount_info = Saved_acc.objects.all()
    for i in support_for_accepting:
        i.accepted = ""
        i.save(update_fields=['accepted'])
    return render(request, "women/redectar_freelancer.html", {"skill_list": skill_list, "username_2": username_2, "acount_info": acount_info, "message": "brrrr", "MEDIA_URL": settings.MEDIA_URL, "support": support})




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
        if i.password != q_2 and i.username != q_1:
            counte += 1
            print("GOOD")
            Login.objects.create(username=q_1, password=q_2,role=roles)

        if age:
            if int(age) < 18:
                return render(request, "women/index.html", {})
    
        if counte == 2:
            counte = 0
            return render(request, 'women/index.html', {'login_info': login_info})

        print(counte)
    return render(request, 'women/register.html')







def remove_tag(request):
    global skill_list,username_2,portfoli_projects,usernames,ava,reputation
    acount_info = Saved_acc.objects.all()
    support = Support.objects.all()
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
    return render(request, 'women/redectar_freelancer.html', {"skill_list": skill_list, "username_2": username_2, "acount_info": acount_info, "message": "brrrr", "MEDIA_URL": settings.MEDIA_URL, "support": support})



def add_tag(request):
    global skill_list,username_2,portfoli_projects,reputation
    acount_info = Saved_acc.objects.all()
    support = Support.objects.all()
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


    return render(request, 'women/redectar_freelancer.html', {"skill_list": skill_list, "username_2": username_2, "acount_info": acount_info, "message": "brrrr", "MEDIA_URL": settings.MEDIA_URL, "support": support})


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
    if new_role:
        user = Login.objects.get(username=new_role)
        user.role = "moderator"
        user.save()
        new_role = ""
    if b1 == "b_1":
        check = "admin"
    elif b2 == "b_2":
        check = "moderator"
    print(check)
    return render(request, "women/staff_login.html")




def moving_to_staff_admin_pannel(request): 
    global check,skill_list,username_2, portfoli_projects,card,salary,usernames,role,new_role
    login_info = Login.objects.all()
    mod_requests = ModeratorAplication.objects.all()
    u_1 = (request.POST.get('username_poll') or '').strip()
    l_1 = (request.POST.get('login_poll') or '').strip()

    
    for i in login_info:
        if check == i.role and u_1 == i.username and l_1 == i.password and check == "admin":
            username_2 = i.username
            return render(request, "women/admin.html", {"username_2": username_2,"mod_requests": mod_requests})
        elif check == i.role and u_1 == i.username and l_1 == i.password and check == "moderator":
            support = Support.objects.all()
            
            username_2 = i.username
            return render(request, "women/moderator.html", {"username_2": username_2,"support": support, })
            

    return render(request, "women/index.html", {})



def moderator_application(request):
    name = (request.POST.get('name') or '').strip()
    age = (request.POST.get('age') or '').strip()
    experience = (request.POST.get('experience') or '').strip()
    reason = (request.POST.get('reason') or '').strip()
    process = (request.POST.get('process') or '').strip()
    violation = (request.POST.get('violation') or '').strip()



    ModeratorAplication.objects.create(name=name, age=age,experience=experience,reason=reason,process=process,violation=violation)


    return render(request, "women/application_for_moderator.html")



def redectar_freelancer(request): 
    global username_2
    acount_info = Saved_acc.objects.all()
    support = Support.objects.all()


    return render(request, "women/redectar_freelancer.html", {"username_2": username_2, "acount_info": acount_info, "message": "brrrr", "MEDIA_URL": settings.MEDIA_URL, "support": support})




def delete_complain(request): 
    support = Support.objects.all()
    ide = (request.POST.get('complain_id') or '').strip()
    c = Support.objects.get(id=ide)  
    c.delete()

    return render(request, "women/moderator.html", {"support": support,})




def accept_complain(request): 
    support = Support.objects.all()
    ide = (request.POST.get('complain_id') or '').strip()
    id = Support.objects.get(id=ide)  
    id.accepted = "accepted"
    id.delete()
    id.save()
    return render(request, "women/moderator.html", {"support": support,"id":id})



def accept_application(request):
    global new_role
    moderator_application = ModeratorAplication.objects.all()
    ide = (request.POST.get('idq') or '').strip()
    id = ModeratorAplication.objects.get(id=ide)  
    new_role = id.name
    print(new_role)
    id.accepted_moder = "accepted"
    id.save()


    return render(request, "women/accepted_moderators.html", {"moderator_app": moderator_application})


def delete_application(request):
    moderator_applicatione = ModeratorAplication.objects.all()
    ide = (request.POST.get('ide') or '').strip()
    app = ModeratorAplication.objects.get(id=ide)
    app.delete()
    return render(request, "women/admin.html", {"mod_requests": moderator_applicatione})


def delete_moderator(request):
    moderator_applicatione = ModeratorAplication.objects.all()
    ide = (request.POST.get('ide') or '').strip()
    app = ModeratorAplication.objects.get(id=ide)
    app.accepted_moder = ""
    print(app.accepted_moder)
    app.save()
    print(app.accepted_moder)
    return render(request, "women/accepted_moderators.html", {"moderator_app": moderator_applicatione})

def block_client(request):
    saved_acc = Saved_acc.objects.all()
    client_id = (request.POST.get('client_id') or '').strip()
    app = Saved_acc.objects.get(id=client_id)
    app.delete()
    return render(request, "women/freelancer_admin_pannel.html", {"saved_acc": saved_acc})


def add_reputation(request):
    saved_acc = Saved_acc.objects.all()
    client_id = (request.POST.get('client_id') or '').strip()
    app = Saved_acc.objects.get(id=client_id)
    for i,v in app.acuonts.items():
        v["reputation"] = "High"

    app.save()
    print(app.acuonts)
    return render(request, "women/freelancer_admin_pannel.html", {"saved_acc": saved_acc})


def punish_freelancer(request):
    saved_acc = Saved_acc.objects.all()
    return render(request, "women/punish_payment.html", {"saved_acc": saved_acc})

def mines_money(request):
    investemoney = InvestedMoney.objects.all()
    punish = (request.POST.get('punish') or '').strip()
    int_punish = int(punish)
    for i in investemoney:
        print(i.money_invested)
        i.money_invested -= int_punish
        print(i.money_invested)
        i.save(update_fields=['money_invested'])
    return render(request, "women/punish_payment.html", {"punish": punish,})




def admin_panel_request_for_moderator(request):
    moderator_applicatione = ModeratorAplication.objects.all()
    return render(request, "women/admin.html", {"mod_requests": moderator_applicatione})

def admin_panel_request_for_accepted_moderators(request):
    moderator_applicatione = ModeratorAplication.objects.all()
    return render(request, "women/accepted_moderators.html", {"moderator_app": moderator_applicatione})

def admin_panel_request_for_freelancer(request):
    saved_acc = Saved_acc.objects.all()
    for i in saved_acc:
        for i,v in i.acuonts.items():
            print(i)
    return render(request, "women/freelancer_admin_pannel.html", {"saved_acc": saved_acc})


def chat_with_offender(request): 
    global name_of_client
    support = Support.objects.all()
    for i in support:
        if name_of_client == i.complain_about_who:
            return redirect('enter_chat_2')
    return render(request, "women/moderator.html", {"support": support})


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
                return render(request, "women/customer.html", {"message": "you don,t have enough money"})
            elif card_number != i.card_number:
                return render(request, "women/customer.html", {"message": "card number is wrong"})
            if i.card_number == card_number and amount <= i.money:
                i.money -= amount
                i.save(update_fields=['money'])
                i.money_invested = amount
                i.save(update_fields=['money_invested'])
                return render(request, "women/customer.html", {"message": "no erros detected", "amount_of_money": i.money_invested})
    return render(request, "women/add_money.html")
    
    


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
            return render(request, "women/support.html", {"support": support})
        return render(request, "women/chat.html", {"messages_from_freelancer": chat, "freelancer_name": username_2})
    return render(request, "women/chat.html",{"messages_from_freelancer": chat, "freelancer_name": username_2})



def save_messages(request):
    global freelancer_data_chat
    chat = Chat.objects.all()
    saved_messages = SaveMesages.objects.all()

    for ie in saved_messages:
        ie.messages_freelancer = freelancer_data_chat
        ie.save(update_fields=['messages_freelancer'])
        print(ie.messages_freelancer)
    return render(request, "women/portfolio.html")







    
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
        return render(request, "women/chat_customer.html", {"messages_client": chat, "client_name": username_2})
    
    return render(request, "women/chat_customer.html",{"messages_client": chat, "client_name": username_2})



def save_messages_2(request):
    global customers_data_chat
    chat = Chat.objects.all()
    saved_messages = SaveMesages.objects.all()

    for ie in saved_messages:
        ie.messages_client = customers_data_chat
        ie.save(update_fields=['messages_client'])
        print(ie.messages_client)
    return render(request, "women/portfolio.html")
    
    
    
def check_tags(request):
    global sorted_clients
    saved_acc = Saved_acc.objects.all()
    for i in saved_acc:
        for name, data in i.acuonts.items():
            sorted_clients[data["username_org"][0]] = data["tags"]
    print(sorted_clients)
    return render(request, "women/customer.html")
    
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
    return render(request, "women/customer.html",)
    
def htmle(request):
    global html
    result = []
    saved_acc = Saved_acc.objects.all()
    for i in saved_acc:
        for ie,v in i.acuonts.items():
            if ie in html:
                print(ie,v)
                result.append(v)
    return render(request, "women/html.html", {"else": result})


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
    return render(request, "women/python.html", {"else": result})
def djangoe(request):
    global django
    result = []
    saved_acc = Saved_acc.objects.all()
    for i in saved_acc:
        for ie,v in i.acuonts.items():
            if ie in django:
                print(ie,v)
                result.append(v)
    return render(request, "women/django.html", {"else": result})
def csse(request):
    global css
    result = []
    saved_acc = Saved_acc.objects.all()
    for i in saved_acc:
        for ie,v in i.acuonts.items():
            if ie in css:
                print(ie,v)
                result.append(v)
    return render(request, "women/css.html", {"else": result})




def select_role(request):
    global role,skill_list,username_2
    acount_info = Saved_acc.objects.all()
    support = Support.objects.all()
    role_1 = (request.POST.get("role") or '').strip()
    role = role_1
    print(role)
    return render(request, "women/redectar_freelancer.html", {"skill_list": skill_list, "username_2": username_2, "acount_info": acount_info, "message": "brrrr", "MEDIA_URL": settings.MEDIA_URL, "support": support,})    

def upload_photo(request):
    global ava
    photos = Photo.objects.all()
    photo_name = request.FILES.get("photoe")
    name_photo = request.POST.get("name_photo")
    ava.append(f"photos/{photo_name.name}")
    print(photo_name, name_photo)
    return render(request, "women/upload_photo.html", {'photos': photos})

def the_photo(request):
    global ava
    ava = []
    photos = Photo.objects.all()
    return render(request, "women/upload_photo.html", {"photos": photos})


def reviews_from_customers(request):
    return render(request, "women/reviews.html")


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
                        return render(request, "women/profiles.html", {"data": data, "photos": photo, "acount_info": data, "chat": chat, "reviews": reviews, "usere": user, "for_who": ie.freelancer, "payment": payment})

    return render(request, "women/customer.html", {"acount_info": data, "chat": chat, "reviews": reviews, "payment": payment})



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
                
    return render(request, "women/reviews.html", {"reviews": reviews, "usere": user, "for_who": for_who})




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
                        changing_number = 0
                        i.save(update_fields=['clients'])
                else:
                    print("not nice")
        

            return render(request, "women/payment.html", {"acount_info": data})
    return render(request, "women/payment.html", {"acount_info": data})



