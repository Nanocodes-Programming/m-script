from django.contrib import admin
from .models import Testimonial, FAQs

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'testi']

@admin.register(FAQs)
class FAQsAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer']