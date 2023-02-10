from django.shortcuts import render
from user.models import Site, InvestmentPlan
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse


def about(request):
    try:
        site = Site.objects.get(pk=1)
    except Site.DoesNotExist:
        site = Site.objects.create(pk=1)
        site.save()

    context ={
        'site':site
    }
    return render(request,'about_us.html',context)

def plans(request):
    try:
        site = Site.objects.get(pk=1)
    except Site.DoesNotExist:
        site = Site.objects.create(pk=1)
        site.save()
    plans = InvestmentPlan.objects.all()
    context ={
        'site':site,
        'plans':plans,
    }
    return render(request,'plans.html',context)

def privacy(request):
    try:
        site = Site.objects.get(pk=1)
    except Site.DoesNotExist:
        site = Site.objects.create(pk=1)
        site.save()
    
    context ={
        'site':site
    }
    return render(request,'privacy.html',context)

def tos(request):
    try:
        site = Site.objects.get(pk=1)
    except Site.DoesNotExist:
        site = Site.objects.create(pk=1)
        site.save()
    
    context ={
        'site':site
    }
    return render(request,'tos.html',context)

def contact(request):
    try:
        site = Site.objects.get(pk=1)
    except Site.DoesNotExist:
        site = Site.objects.create(pk=1)
        site.save()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry"
            body = {
            'subject': form.cleaned_data['subject'],
            'name': form.cleaned_data['name'],
            'sender': form.cleaned_data['sender'],
            'message':form.cleaned_data['message'],
            }

            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'benjaminservices03@gmail.com', [''])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
    else:
        form = ContactForm()
    context ={
        'form': form,
        'site':site,
    }
    return render(request,'contact.html',context)


def faq(request):
    try:
        site = Site.objects.get(pk=1)
    except Site.DoesNotExist:
        site = Site.objects.create(pk=1)
        site.save()
    
    context ={
        'site':site
    }
    return render(request,'faq.html',context)
                
                
def index(request):
    try:
        site = Site.objects.get(pk=1)
    except Site.DoesNotExist:
        site = Site.objects.create(pk=1)
        site.save()
    plans = InvestmentPlan.objects.all()
    context ={
        'site':site,
        'plans':plans
    }
    return render(request,'index.html',context)
                
                
def partnership(request):
    try:
        site = Site.objects.get(pk=1)
    except Site.DoesNotExist:
        site = Site.objects.create(pk=1)
        site.save()
    
    context ={
        'site':site
    }
    return render(request,'partnership.html',context)
                
                
                
def terms(request):
    try:
        site = Site.objects.get(pk=1)
    except Site.DoesNotExist:
        site = Site.objects.create(pk=1)
        site.save()
    
    context ={
        'site':site
    }
    return render(request,'terms.html',context)


