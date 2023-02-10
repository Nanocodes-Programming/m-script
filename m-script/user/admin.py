from django.contrib import admin
from user.models import Profile,Referral,Notification,Deposit,WalletAddress,Withdraw,Transfer,InvestmentPlan,Site,SendEmail, Kyc, InvestmentCategory
from django import forms
from django.contrib import admin
from django.contrib.auth.models import User
from django.conf import settings

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    pass

@admin.register(Deposit)
class DepositAdmin(admin.ModelAdmin):
    list_display = ('profile','wallet_address','amount','wallet_type','time','verified','usdt_amount')
    list_editable=  ('verified',)

@admin.register(WalletAddress)
class WalletAddressAdmin(admin.ModelAdmin):
    list_display = ('address','bitcoin_address','litecoin_address','xrp_address','etherum_address','usdt_address')
    list_editable=  ('bitcoin_address','litecoin_address','xrp_address','etherum_address','usdt_address')
    list_display_links = ('address',)
    
@admin.register(Withdraw)
class WithdrawAdmin(admin.ModelAdmin):
    list_display = ('profile','wallet_address','amount','wallet_type','time','verified')
    list_editable=  ('verified',)
    
@admin.register(Transfer)
class TransferAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'amount','time','verified')
    list_editable=  ('verified',)
    
@admin.register(InvestmentPlan)
class InvestmentPlanAdmin(admin.ModelAdmin):
    pass

# @admin.register(PlanType)
# class PlanTypeAdmin(admin.ModelAdmin):
#     pass

@admin.register(Kyc)
class KycAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','address','verified')
    list_editable=  ('verified',)

@admin.register(Referral)
class ReferralAdmin(admin.ModelAdmin):
    pass

@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = ('owned_by','name','email','address','second_address','logo','phone_number')
    list_editable = ('name','email','address','second_address','logo','phone_number')
    list_display_links = ('owned_by',)
    
@admin.register(SendEmail) 
class SendEmailAdmin(admin.ModelAdmin):
    list_display = ('username','email','subject','content')
    list_editable = ('subject','content')
    list_display_links = ('username',)

class InvestmentCategory(admin.ModelAdmin):
    list_display = ('title')
    list_editable = ('title')
    list_display_links = ('titlt',)
    prepopulated_fields = {"slug": ("title",)}
