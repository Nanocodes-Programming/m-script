from django.urls import path
from . import views


urlpatterns = [
    path('about',views.about, name='about-us'),
    path('contact',views.contact, name='contact'),
    path('faq',views.faq, name='faq'),
    path('',views.index, name='home'),
    path('partnership',views.partnership, name='partnership'),
    path('terms',views.terms, name='terms'),
    path('plans',views.plans, name='plans'),
    path('privacy',views.privacy, name='privacy'),
    path('terms-of-service',views.tos, name='tos'),

]
