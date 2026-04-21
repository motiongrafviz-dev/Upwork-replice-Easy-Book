from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', main, name='home'),
    path('register/', register, name='register'),
    path('register_pole/', register_pole, name='register_pole'),
    path('login/', login, name='login'),
    path('checks_who_are_you/', checks_who_are_you, name='checks_who_are_you'),
    path('remove_tag/', remove_tag, name='remove_tag'),
    path('add_tag/', add_tag, name='add_tag'),
    path('portfolio/', portfolio, name='portfolio'),
    path('add_page/', add_page, name='add_page'),
    path('project_1/', project_1, name='project_1'),
    path('project_2/', project_2, name='project_2'),
    path('acc_apply/', acc_apply, name='acc_apply'),
    path('price_per_project/', price_per_project, name='price_per_project'),
    path('hire_freelancer/', hire_freelancer, name='hire_freelancer'),
    path('save_messages/', save_messages, name='save_messages'),
    path('enter_chat/', enter_chat, name='enter_chat'),
    path('enter_chat_2/', enter_chat_2, name='enter_chat_2'),
    path('moderator_application/', moderator_application, name='moderator_application'),

]
