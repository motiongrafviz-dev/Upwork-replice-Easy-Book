from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', main, name='index'),
    path('staff_login/', staff_login, name='staff_login'),
    path('delete_complain/', delete_complain, name='delete_complain'),
    path('accept_complain/', accept_complain, name='accept_complain'),
    path('moving_to_staff_admin_pannel/', moving_to_staff_admin_pannel, name='moving_to_staff_admin_pannel'),
    path('chat_with_offender/', chat_with_offender, name='chat_with_offender'),
    path('accept_application/', accept_application, name='accept_application'),
    path('delete_application/', delete_application, name='delete_application'),
    path('delete_moderator/', delete_moderator, name='delete_moderator'),
    path('block_client/', block_client, name='block_client'),
    path('admin_panel_request_for_moderator/', admin_panel_request_for_moderator, name='admin_panel_request_for_moderator'),
    path('admin_panel_request_for_freelancer/', admin_panel_request_for_freelancer, name='admin_panel_request_for_freelancer'),
    path('add_reputation/', add_reputation, name='add_reputation'),
    path('punish_freelancer/', punish_freelancer, name='punish_freelancer'),
    path('mines_money/', mines_money, name='mines_money'),
    path('admin_panel_request_for_accepted_moderators/', admin_panel_request_for_accepted_moderators, name='admin_panel_request_for_accepted_moderators'),
]
