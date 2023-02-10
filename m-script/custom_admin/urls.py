from django.urls import path
from . import views


urlpatterns = [
    path("", views.adminhome, name='adminhome'),
    path("login/", views.login, name="login"),
    path('all-accounts', views.adminallaccount, name='admin-allaccount'),
    path('active-accounts', views.adminactiveaccount, name='admin-activeaccount'),
    path('deactivated-accounts', views.admindeactivatedaccount, name='admin-deactivatedaccount'),

    path('all-deposit', views.adminalldeposit, name='admin-alldeposit'),
    path('active-deposit', views.adminactivedeposit, name='admin-activedeposit'),
    path('completed-deposit', views.admincompleteddeposit, name='admin-completeddeposit'),
    path('pending-deposit', views.adminpendingdeposit, name='admin-pendingdeposit'),

    path('all-withdraw', views.adminallwithdrawal, name='admin-allwithdraw'),
    path('completed-withdraw', views.admincompletedwithdrawal, name='admin-completedwithdraw'),
    path('pending-withdraw', views.adminpendingwithdrawal, name='admin-pendingwithdraw'),

    path('all-transaction', views.adminalltransaction, name='admin-alltransaction'),
    path('completed-transaction', views.admincompletedtransaction, name='admin-completedtransaction'),
    path('pending-transaction', views.adminpendingtransaction, name='admin-pendingtransaction'),

    path('deposit-plan', views.adminsetting_depositplan, name='adminsetting_depositplan'),
    path('add-testimonial', views.adminsetting_addtesti, name='adminsetting_addtesti'),
    path('add-faqs', views.adminsetting_addfaqs, name='adminsetting_addfaqs'),
    path('set-charges', views.adminsetting_setcharges, name='adminsetting_setcharges'),
    path('extra-statistics', views.adminsetting_extrastat, name='adminsetting_extrastat'),

    path('send-bonus', views.adminsendbonus, name='admin-sendbonus'),
    path('send-penalty', views.adminsendpenalty, name='admin-sendpenalty'),

    path('read-messages', views.adminreadmessage, name='admin-readmessages'),
    path('send-mail', views.adminsendmail, name='admin-sendmail'),

]