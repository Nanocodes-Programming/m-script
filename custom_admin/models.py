from django.db import models

class Testimonial(models.Model):
    name = models.CharField(max_length=50)
    testi = models.TextField()
    image = models.ImageField(blank=True, null=True) 

class FAQs(models.Model):
    question = models.CharField(max_length=100)
    answer = models.TextField()

class Charges(models.Model):
    deposit_charges = models.IntegerField()
    withdrawal_charges = models.IntegerField()