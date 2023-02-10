from django.shortcuts import render
from user.models import WalletAddress,Deposit,Profile,Notification,Withdraw,Transfer, Transaction, InvestmentPlan,Referral,Site, Kyc, SendEmail
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import get_user_model
from datetime import timedelta,date
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
User = get_user_model()
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from custom_admin.models import Testimonial, FAQs, Charges
# Create your views here

def adminhome(request):
    return render(request,'admin_temp/index.html')

def adminallaccount(request):
    return render(request,'admin_temp/users.html')

def adminactiveaccount(request):
    return render(request,'admin_temp/users2.html')

def admindeactivatedaccount(request):
    return render(request,'admin_temp/users3.html')

def user_deposit(request):
    pass
    
class AllDeposit(LoginRequiredMixin, ListView):
    template_name = 'admin_temp/deposit.html'
    model = Deposit
    context_object_name = 'deposits'

# def adminalldeposit(request):
#     user = User.objects.get(username = request.user.username)
    
#     try:
#         site = Site.objects.get(pk=1)
#     except Site.DoesNotExist:
#         site = Site.objects.create(pk=1)
#         site.save()
        
#     if not Profile.objects.filter(user= user.id):
#         return redirect('/user/profile')
    
#     profile = Profile.objects.get(user=user)
#     deposits = Deposit.objects.filter(profile=profile).order_by('-time')[:5]
#     try:
#         wallet = WalletAddress.objects.get(id=1)
#     except WalletAddress.DoesNotExist:
#         wallet = WalletAddress.objects.create(pk=1)
#         wallet.save()
#     notifications_unread_count = Notification.objects.filter(profile=profile,read='False').count()
#     notifications_unread = Notification.objects.filter(profile=profile,read='False').order_by('-time')[:3]
#     context = {
#         'wallet':wallet,
#         'deposits': deposits,
#         'profile':profile,
#         'notifications_unread_count':notifications_unread_count,
#         'notifications_unread': notifications_unread,
#         'site':site
#     }
#     if request.method == 'POST':
#         wallet_address = request.POST['wallet_address']
#         amount = request.POST['amount']
#         wallet_type = request.POST['wallet_type']
#         usdt_amount = request.POST['usdt_amount']
#         deposit = Deposit.objects.create(profile=profile,amount=amount,wallet_type=wallet_type,wallet_address=wallet_address,usdt_amount=usdt_amount)
#         deposit.save()
#         action = f'You have deposited {amount} {wallet_type} into {wallet_address}'
#         action_title = 'Deposit Pending'
#         notification = Notification.objects.create(profile=profile,action_title=action_title,action=action)
#         notification.save()
#         transaction = Transaction.objects.create(profile=profile,category='deposit',action_title='Deposit Requested',action=action)
#         transaction.save()
#         # body = f'{profile.user.username} has deposited {deposit.amount} {deposit.wallet_type} into {deposit.wallet_address}'
#         # body_two = f'You have deposited {deposit.amount} {deposit.wallet_type} into {deposit.wallet_address}'
#         # subject = 'Deposit Requested'
#         # # send_mail(subject=subject,message=body,from_email=settings.EMAIL_HOST_USER,recipient_list=[settings.RECIPIENT_ADDRESS])
#         # # send_mail(subject=subject,message=body_two,from_email=settings.EMAIL_HOST_USER,recipient_list=[request.user.email])
#         # send_email(subject,body,settings.RECIPIENT_ADDRESS)
        
#         # send_email(subject,body_two,request.user.email)
#         # messages.info(request, 'You have applied for a deposit')
#         return redirect('/user/deposit')
        
#     return render(request,'admin_temp/deposit.html',context)
#     # return render(request,'admin_temp/deposit.html')

class ActiveDeposit(LoginRequiredMixin, ListView):
    template_name = 'admin_temp/deposit2.html'
    model = Deposit
    context_object_name = 'deposits'

# def adminactivedeposit(request):
#     user = User.objects.get(username = request.user.username)
    
#     try:
#         site = Site.objects.get(pk=1)
#     except Site.DoesNotExist:
#         site = Site.objects.create(pk=1)
#         site.save()
        
#     if not Profile.objects.filter(user= user.id):
#         return redirect('/user/profile')
    
#     profile = Profile.objects.get(user=user)
#     deposits = Deposit.objects.filter(profile=profile).order_by('-time')[:5]
#     try:
#         wallet = WalletAddress.objects.get(id=1)
#     except WalletAddress.DoesNotExist:
#         wallet = WalletAddress.objects.create(pk=1)
#         wallet.save()
#     notifications_unread_count = Notification.objects.filter(profile=profile,read='False').count()
#     notifications_unread = Notification.objects.filter(profile=profile,read='False').order_by('-time')[:3]
#     context = {
#         'wallet':wallet,
#         'deposits': deposits,
#         'profile':profile,
#         'notifications_unread_count':notifications_unread_count,
#         'notifications_unread': notifications_unread,
#         'site':site
#     }
#     if request.method == 'POST':
#         wallet_address = request.POST['wallet_address']
#         amount = request.POST['amount']
#         wallet_type = request.POST['wallet_type']
#         usdt_amount = request.POST['usdt_amount']
#         deposit = Deposit.objects.create(profile=profile,amount=amount,wallet_type=wallet_type,wallet_address=wallet_address,usdt_amount=usdt_amount)
#         deposit.save()
#         action = f'You have deposited {amount} {wallet_type} into {wallet_address}'
#         action_title = 'Deposit Pending'
#         notification = Notification.objects.create(profile=profile,action_title=action_title,action=action)
#         notification.save()
#         transaction = Transaction.objects.create(profile=profile,category='deposit',action_title='Deposit Requested',action=action)
#         transaction.save()
#         # body = f'{profile.user.username} has deposited {deposit.amount} {deposit.wallet_type} into {deposit.wallet_address}'
#         # body_two = f'You have deposited {deposit.amount} {deposit.wallet_type} into {deposit.wallet_address}'
#         # subject = 'Deposit Requested'
#         # # send_mail(subject=subject,message=body,from_email=settings.EMAIL_HOST_USER,recipient_list=[settings.RECIPIENT_ADDRESS])
#         # # send_mail(subject=subject,message=body_two,from_email=settings.EMAIL_HOST_USER,recipient_list=[request.user.email])
#         # send_email(subject,body,settings.RECIPIENT_ADDRESS)
        
#         # send_email(subject,body_two,request.user.email)
#         # messages.info(request, 'You have applied for a deposit')
#         return redirect('/user/deposit')
        
#     return render(request,'admin_temp/deposit2.html',context)
#     # return render(request,'admin_temp/deposit2.html')

def admincompleteddeposit(request):
    return render(request,'admin_temp/deposit3.html')

class PendingDeposit(LoginRequiredMixin, ListView):
    template_name = 'admin_temp/deposit4.html'
    model = Deposit
    context_object_name = 'deposits'

# def adminpendingdeposit(request):
#     user = User.objects.get(username = request.user.username)
    
#     try:
#         site = Site.objects.get(pk=1)
#     except Site.DoesNotExist:
#         site = Site.objects.create(pk=1)
#         site.save()
        
#     if not Profile.objects.filter(user= user.id):
#         return redirect('/user/profile')
    
#     profile = Profile.objects.get(user=user)
#     deposits = Deposit.objects.filter(profile=profile).order_by('-time')[:5]
#     try:
#         wallet = WalletAddress.objects.get(id=1)
#     except WalletAddress.DoesNotExist:
#         wallet = WalletAddress.objects.create(pk=1)
#         wallet.save()
#     notifications_unread_count = Notification.objects.filter(profile=profile,read='False').count()
#     notifications_unread = Notification.objects.filter(profile=profile,read='False').order_by('-time')[:3]
#     context = {
#         'wallet':wallet,
#         'deposits': deposits,
#         'profile':profile,
#         'notifications_unread_count':notifications_unread_count,
#         'notifications_unread': notifications_unread,
#         'site':site
#     }
#     if request.method == 'POST':
#         wallet_address = request.POST['wallet_address']
#         amount = request.POST['amount']
#         wallet_type = request.POST['wallet_type']
#         usdt_amount = request.POST['usdt_amount']
#         deposit = Deposit.objects.create(profile=profile,amount=amount,wallet_type=wallet_type,wallet_address=wallet_address,usdt_amount=usdt_amount)
#         deposit.save()
#         action = f'You have deposited {amount} {wallet_type} into {wallet_address}'
#         action_title = 'Deposit Pending'
#         notification = Notification.objects.create(profile=profile,action_title=action_title,action=action)
#         notification.save()
#         transaction = Transaction.objects.create(profile=profile,category='deposit',action_title='Deposit Requested',action=action)
#         transaction.save()
#         # body = f'{profile.user.username} has deposited {deposit.amount} {deposit.wallet_type} into {deposit.wallet_address}'
#         # body_two = f'You have deposited {deposit.amount} {deposit.wallet_type} into {deposit.wallet_address}'
#         # subject = 'Deposit Requested'
#         # # send_mail(subject=subject,message=body,from_email=settings.EMAIL_HOST_USER,recipient_list=[settings.RECIPIENT_ADDRESS])
#         # # send_mail(subject=subject,message=body_two,from_email=settings.EMAIL_HOST_USER,recipient_list=[request.user.email])
#         # send_email(subject,body,settings.RECIPIENT_ADDRESS)
        
#         # send_email(subject,body_two,request.user.email)
#         # messages.info(request, 'You have applied for a deposit')
#         return redirect('/user/deposit')
        
#     return render(request,'admin_temp/deposit4.html',context)
#     # return render(request,'admin_temp/deposit4.html')


class AllWithdraw(LoginRequiredMixin, ListView):
    template_name = 'admin_temp/withdraw.html'
    model = Withdraw
    context_object_name = 'withdraws'

# def adminallwithdrawal(request):
#     user = User.objects.get(username = request.user.username)
    
#     try:
#         site = Site.objects.get(pk=1)
#     except Site.DoesNotExist:
#         site = Site.objects.create(pk=1)
#         site.save()
        
#     if not Profile.objects.filter(user= user.id):
#         return redirect('/user/profile')
    
#     profile = Profile.objects.get(user=user)
#     notifications_unread_count = Notification.objects.filter(profile=profile,read='False').count()
#     notifications_unread = Notification.objects.filter(profile=profile,read='False').order_by('-time')[:3]
#     withdraws = Withdraw.objects.filter(profile=profile).order_by('-time')[:5]
#     try:
#         wallet = WalletAddress.objects.get(id=1)
#     except WalletAddress.DoesNotExist:
#         wallet = WalletAddress.objects.create(pk=1)
#         wallet.save()
#     context = {
#         'profile':profile,
#         'wallet':wallet,
#         'withdraws': withdraws,
#         'notifications_unread_count':notifications_unread_count,
#         'notifications_unread': notifications_unread,
#         'site':site
#     }
#     if request.method == 'POST':
#         # if profile.plan_name:
#         #     messages.info(request, 'You have an existing plan')
#         #     return render(request,'user/withdraw.html',context)
#         wallet_address = request.POST['wallet_address']
#         if wallet_address == None or wallet_address =='':
#             messages.info(request, 'You did not add a withdrawal address')
#             return redirect('/user/withdraw')
#         amount = request.POST['amount']
#         wallet_type = request.POST['wallet_type']
#         usdt_amount = request.POST['usdt_amount']
#         if float(usdt_amount) > profile.available_balance:
#             messages.info(request, 'Your have insufficient funds')
#             return redirect('/user/withdraw')
            
#         withdraw = Withdraw.objects.create(profile=profile,amount=amount,wallet_type=wallet_type,wallet_address=wallet_address,usdt_amount=usdt_amount)
#         withdraw.save()
#         action = f'You has withdrawn {amount} {wallet_type} into {wallet_address}'
#         action_title = 'Withdrawal Pending'
#         notification = Notification.objects.create(profile=profile,action_title=action_title,action=action)
#         notification.save()
#         transaction = Transaction.objects.create(profile=profile,category='withdraw',action_title='Withdraw Requested',action=action)
#         transaction.save()
#         # body = f'{profile.user.username} has withdrawn {withdraw.amount} {withdraw.wallet_type} into {withdraw.wallet_address}'
#         # body_two = f'You have withdrawn {withdraw.amount} {withdraw.wallet_type} into {withdraw.wallet_address}'
#         # subject = 'Withdrawal Requested'
#         # #send_mail(subject=subject,message=body,from_email=settings.EMAIL_HOST_USER,recipient_list=[settings.RECIPIENT_ADDRESS])
#         # #send_mail(subject=subject,message=body_two,from_email=settings.EMAIL_HOST_USER,recipient_list=[request.user.email])
#         # send_email(subject,body,settings.RECIPIENT_ADDRESS)
#         # send_email(subject,body_two,request.user.email)
#         # messages.info(request, 'You have applied for withdrawal')
#         return redirect('/user/withdraw') 
#     return render(request,'admin_temp/withdraw.html',context)
#     # return render(request,'admin_temp/withdraw.html')

class CompletedWithdraw(LoginRequiredMixin, ListView):
    template_name = 'admin_temp/withdraw2.html'
    model = Withdraw
    context_object_name = 'withdraws'

# def admincompletedwithdrawal(request):
#     user = User.objects.get(username = request.user.username)
    
#     try:
#         site = Site.objects.get(pk=1)
#     except Site.DoesNotExist:
#         site = Site.objects.create(pk=1)
#         site.save()
        
#     if not Profile.objects.filter(user= user.id):
#         return redirect('/user/profile')
    
#     profile = Profile.objects.get(user=user)
#     notifications_unread_count = Notification.objects.filter(profile=profile,read='False').count()
#     notifications_unread = Notification.objects.filter(profile=profile,read='False').order_by('-time')[:3]
#     withdraws = Withdraw.objects.filter(profile=profile).order_by('-time')[:5]
#     try:
#         wallet = WalletAddress.objects.get(id=1)
#     except WalletAddress.DoesNotExist:
#         wallet = WalletAddress.objects.create(pk=1)
#         wallet.save()
#     context = {
#         'profile':profile,
#         'wallet':wallet,
#         'withdraws': withdraws,
#         'notifications_unread_count':notifications_unread_count,
#         'notifications_unread': notifications_unread,
#         'site':site
#     }
#     if request.method == 'POST':
#         # if profile.plan_name:
#         #     messages.info(request, 'You have an existing plan')
#         #     return render(request,'user/withdraw.html',context)
#         wallet_address = request.POST['wallet_address']
#         if wallet_address == None or wallet_address =='':
#             messages.info(request, 'You did not add a withdrawal address')
#             return redirect('/user/withdraw')
#         amount = request.POST['amount']
#         wallet_type = request.POST['wallet_type']
#         usdt_amount = request.POST['usdt_amount']
#         if float(usdt_amount) > profile.available_balance:
#             messages.info(request, 'Your have insufficient funds')
#             return redirect('/user/withdraw')
            
#         withdraw = Withdraw.objects.create(profile=profile,amount=amount,wallet_type=wallet_type,wallet_address=wallet_address,usdt_amount=usdt_amount)
#         withdraw.save()
#         action = f'You has withdrawn {amount} {wallet_type} into {wallet_address}'
#         action_title = 'Withdrawal Pending'
#         notification = Notification.objects.create(profile=profile,action_title=action_title,action=action)
#         notification.save()
#         transaction = Transaction.objects.create(profile=profile,category='withdraw',action_title='Withdraw Requested',action=action)
#         transaction.save()
#         # body = f'{profile.user.username} has withdrawn {withdraw.amount} {withdraw.wallet_type} into {withdraw.wallet_address}'
#         # body_two = f'You have withdrawn {withdraw.amount} {withdraw.wallet_type} into {withdraw.wallet_address}'
#         # subject = 'Withdrawal Requested'
#         # #send_mail(subject=subject,message=body,from_email=settings.EMAIL_HOST_USER,recipient_list=[settings.RECIPIENT_ADDRESS])
#         # #send_mail(subject=subject,message=body_two,from_email=settings.EMAIL_HOST_USER,recipient_list=[request.user.email])
#         # send_email(subject,body,settings.RECIPIENT_ADDRESS)
#         # send_email(subject,body_two,request.user.email)
#         # messages.info(request, 'You have applied for withdrawal')
#         return redirect('/user/withdraw') 
#     return render(request,'admin_temp/withdraw2.html',context)
#     # return render(request,'admin_temp/withdraw2.html')

class PendingWithdraw(LoginRequiredMixin, ListView):
    template_name = 'admin_temp/withdraw3.html'
    model = Withdraw
    context_object_name = 'withdraws'

# def adminpendingwithdrawal(request):
#     user = User.objects.get(username = request.user.username)
    
#     try:
#         site = Site.objects.get(pk=1)
#     except Site.DoesNotExist:
#         site = Site.objects.create(pk=1)
#         site.save()
        
#     if not Profile.objects.filter(user= user.id):
#         return redirect('/user/profile')
    
#     profile = Profile.objects.get(user=user)
#     notifications_unread_count = Notification.objects.filter(profile=profile,read='False').count()
#     notifications_unread = Notification.objects.filter(profile=profile,read='False').order_by('-time')[:3]
#     withdraws = Withdraw.objects.filter(profile=profile).order_by('-time')[:5]
#     try:
#         wallet = WalletAddress.objects.get(id=1)
#     except WalletAddress.DoesNotExist:
#         wallet = WalletAddress.objects.create(pk=1)
#         wallet.save()
#     context = {
#         'profile':profile,
#         'wallet':wallet,
#         'withdraws': withdraws,
#         'notifications_unread_count':notifications_unread_count,
#         'notifications_unread': notifications_unread,
#         'site':site
#     }
#     if request.method == 'POST':
#         # if profile.plan_name:
#         #     messages.info(request, 'You have an existing plan')
#         #     return render(request,'user/withdraw.html',context)
#         wallet_address = request.POST['wallet_address']
#         if wallet_address == None or wallet_address =='':
#             messages.info(request, 'You did not add a withdrawal address')
#             return redirect('/user/withdraw')
#         amount = request.POST['amount']
#         wallet_type = request.POST['wallet_type']
#         usdt_amount = request.POST['usdt_amount']
#         if float(usdt_amount) > profile.available_balance:
#             messages.info(request, 'Your have insufficient funds')
#             return redirect('/user/withdraw')
            
#         withdraw = Withdraw.objects.create(profile=profile,amount=amount,wallet_type=wallet_type,wallet_address=wallet_address,usdt_amount=usdt_amount)
#         withdraw.save()
#         action = f'You has withdrawn {amount} {wallet_type} into {wallet_address}'
#         action_title = 'Withdrawal Pending'
#         notification = Notification.objects.create(profile=profile,action_title=action_title,action=action)
#         notification.save()
#         transaction = Transaction.objects.create(profile=profile,category='withdraw',action_title='Withdraw Requested',action=action)
#         transaction.save()
#         # body = f'{profile.user.username} has withdrawn {withdraw.amount} {withdraw.wallet_type} into {withdraw.wallet_address}'
#         # body_two = f'You have withdrawn {withdraw.amount} {withdraw.wallet_type} into {withdraw.wallet_address}'
#         # subject = 'Withdrawal Requested'
#         # #send_mail(subject=subject,message=body,from_email=settings.EMAIL_HOST_USER,recipient_list=[settings.RECIPIENT_ADDRESS])
#         # #send_mail(subject=subject,message=body_two,from_email=settings.EMAIL_HOST_USER,recipient_list=[request.user.email])
#         # send_email(subject,body,settings.RECIPIENT_ADDRESS)
#         # send_email(subject,body_two,request.user.email)
#         # messages.info(request, 'You have applied for withdrawal')
#         return redirect('/user/withdraw') 
#     return render(request,'admin_temp/withdraw3.html',context)
#     # return render(request,'admin_temp/withdraw3.html')

class AllTransaction(LoginRequiredMixin, ListView):
    template_name = 'admin_temp/transaction.html'
    model = Notification
    context_object_name = 'transactions'

# def adminalltransaction(request):
#     user = User.objects.get(username = request.user.username)
    
#     try:
#         site = Site.objects.get(pk=1)
#     except Site.DoesNotExist:
#         site = Site.objects.create(pk=1)
#         site.save()
           
#     if not Profile.objects.filter(user= user.id):
#         return redirect('/user/profile')
    
#     profile = Profile.objects.get(user=user)
#     notifications_unread_count = Notification.objects.filter(profile=profile,read='False').count()
#     notifications_unread = Notification.objects.filter(profile=profile,read='False').order_by('-time')[:3]
#     transactions = Transaction.objects.filter(profile=profile).order_by('-time')
#     category = request.GET.get('category')
#     if category:
#         transactions = Transaction.objects.filter(profile=profile,category=category).order_by('-time')
    
#     context = {
#         'profile':profile,
#         'transactions':transactions,
#         'notifications_unread_count':notifications_unread_count,
#         'notifications_unread': notifications_unread,
#         'site':site
#     }
#     return render(request,'admin_temp/transaction.html',context) 
#     # return render(request,'admin_temp/transaction.html')

def admincompletedtransaction(request):
    return render(request,'admin_temp/transaction2.html')

def adminpendingtransaction(request):
    return render(request,'admin_temp/transaction3.html')

class DepositPlan(LoginRequiredMixin, ListView):
    template_name = 'admin_temp/setting.html'
    model = InvestmentPlan
    context_object_name = 'plans'

# def adminsetting_depositplan(request):
#     return render(request,'admin_temp/setting.html')

class FeedBack(LoginRequiredMixin, ListView):
    template_name = 'admin_temp/setting2.html'
    model = Testimonial
    context_object_name = 'testimonials'
# def adminsetting_addtesti(request):
#     return render(request,'admin_temp/setting2.html')

class AdminFaqs(LoginRequiredMixin, ListView):
    template_name = 'admin_temp/setting3.html'
    model = FAQs
    context_object_name = 'faqs'
# def adminsetting_addfaqs(request):
#     return render(request,'admin_temp/setting3.html')

def adminsetting_setcharges(request):
    return render(request,'admin_temp/setting4.html')

def adminsetting_extrastat(request):
    return render(request,'admin_temp/setting5.html')

def adminsendbonus(request):
    return render(request,'admin_temp/bonus.html')

def adminsendpenalty(request):
    return render(request,'admin_temp/bonus2.html')

class ReadMessages(LoginRequiredMixin, ListView):
    template_name = 'admin_temp/msg.html'
    model = SendEmail
    context_object_name = 'messages'
# def adminreadmessage(request):
#     return render(request,'admin_temp/msg.html')

def adminsendmail(request):
    return render(request,'admin_temp/msg2.html')