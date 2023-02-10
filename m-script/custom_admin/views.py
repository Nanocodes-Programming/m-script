from django.shortcuts import render, redirect
# from django.contrib.auth.models import *
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from user.models import *
from .models import *
# Create your views here.
# def login(request):
# #    try:
       
#        if request.user.is_authenticated and request.user.is_superuser:
#             return redirect("admin/")
       
#        if request.method == "POST":
#            username = request.POST.get("username")
#            password = request.POST.get("password")
#            user_obj = User.objects.get(username=username).lower()

#            if not user_obj.exists():
#                messages.info(request, "Account not found!!")

#            user_obj = authenticate(username=username, password=password)
           
#            # login the request user
#            if user_obj and user_obj.is_superuser:
#                login(request)
#                messages.info(request, "Login Successfull!!")
#                return redirect("/")
#    except Exception as e:
#         print(f"An error occured, whose name is {e}".user
#    if request.user.is_authenticated:
#        return redirect("/admin/dashboard")
#    if request.method == "POST":
#        username = request.POST.get("username")
#        password = request.POST.get("password")
#        user = User.objects.get(username=username)

#        user = authenticate(request, username=username, password=password)
#        if user:
#            login(request)
#            messages.info(request, "Login successfully")
#            return redirect("/admin/dashboard")
#    return render(request, 'admin2/login.html',{})

# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request)
#             return redirect('/admin/dashboard/')
#         else:
#             return render(request, 'admin2/login.html', {'error': 'Invalid credentials'})
#     else:
#         return render(request, 'admin2/login.html')



# @login_required(login_url='/admin/login')
def adminhome(request):
    return render(request,'admin2/index.html')

# @login_required(login_url='/admin/login')
def adminallaccount(request):
    user = User.objects.all()
    profile = Profile.objects.all()
    context = {'user':user, 'profile':profile}
    return render(request,'admin2/users.html', context)

def adminactiveaccount(request):
    user = User.objects.all()
    profile = Profile.objects.all()
    context = {'user':user, 'profile':profile}
    return render(request,'admin2/users2.html', context)

def admindeactivatedaccount(request):
    user = User.objects.all( )
    profile = Profile.objects.all()
    context = {'user':user, 'profile':profile}
    return render(request,'admin2/users3.html', context)

def adminalldeposit(request):
    return render(request,'admin2/deposit.html')

def adminactivedeposit(request):
    return render(request,'admin2/deposit2.html')

def admincompleteddeposit(request):
    return render(request,'admin2/deposit3.html')

def adminpendingdeposit(request):
    return render(request,'admin2/deposit4.html')

def adminallwithdrawal(request):
    return render(request,'admin2/withdraw.html')

def admincompletedwithdrawal(request):
    return render(request,'admin2/withdraw2.html')

def adminpendingwithdrawal(request):
    return render(request,'admin2/withdraw3.html')

def adminalltransaction(request):
    return render(request,'admin2/transaction.html')

def admincompletedtransaction(request):
    return render(request,'admin2/transaction2.html')

def adminpendingtransaction(request):
    return render(request,'admin2/transaction3.html')

def adminsetting_depositplan(request):
    return render(request,'admin2/setting.html')

def adminsetting_addtesti(request):
    return render(request,'admin2/setting2.html')

def adminsetting_addfaqs(request):
    return render(request,'admin2/setting3.html')

def adminsetting_setcharges(request):
    return render(request,'admin2/setting4.html')

def adminsetting_extrastat(request):
    return render(request,'admin2/setting5.html')

def adminsendbonus(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        bonus_amount = float(request.POST.get('bonus_amount'))
        
        try:
            user = User.objects.get(email=email)
            user_p = Profile.objects.get(user=user)
            user_p.bonus += bonus_amount
            user_p.save()
            message = f'Bonus of ${bonus_amount} has been sent to {email}'
            transaction = Transaction.objects.create(
                profile=user_p,
                category="Bonus From Admin",
                action_title="Bonus  Reward",
                action="Bonus creditted from admin"
            )
            body = f"Admin has sent Bonus reward of {transfer.amount}USD to {transfer_user.user.email}"
            body_two = f"Admin has sent Bonus reward of  {transfer.amount}USD to {transfer_user.user.email}"
            body_three = f"Admin has sent Bonus reward of {transfer.amount}USD to {transfer_user.user.email}"
            subject = "Transfer Requested"
            send_email(subject, body, settings.RECIPIENT_ADDRESS)
            send_email(subject, body_three, user_p.user.email)
            messages.info(request, 'You have applied sent reward successfully')
            return redirect('/admin/')
        except User.DoesNotExist:
            message = f'User with email {email} does not exist.'
        
        return render(request, 'admin2/bonus.html', {'message': message})
    
    return render(request, 'admin2/bonus.html')


def adminsendpenalty(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        amount = float(request.POST.get('amount'))
        
        try:
            user = User.objects.get(email=email)
            user_p = Profile.objects.get(user=user)
            if user_p.available_balance >= amount:
                user_p.available_balance -= amount
                user_p.save()
                message = f'${amount} has been deducted from {email} from the admin because He/ She violated some rules!!'
            else:
                message = f'User with email {email} does not have sufficient balance.'
        except User.DoesNotExist:
            message = f'User with email {email} does not exist.'
        
        return render(request, 'admin2/bonus2.html', {'message': message})
    
    return render(request, 'admin2/bonus2.html')


def adminreadmessage(request):
    return render(request,'admin2/msg.html')

def adminsendmail(request):
    return render(request,'admin2/msg2.html')