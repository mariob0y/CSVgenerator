from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator

from django.conf import settings

CHOICES = (

    ('1', 'Choose...'),
    ('2', 'name'),
    ('3', 'job'),
    ('4', 'company'),
    ('5', 'date'),
    ('6', 'phone'),
    ('7', 'address'),
    ('8', 'city'),
    ('9', 'country'),
    ('10', 'email')

    )


class Scheme(models.Model):

    upload = models.FileField(upload_to='', blank=True)

    name = models.CharField(max_length=30, default="None", blank=False)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=1
    )

    c1 = models.CharField(max_length=30, choices=CHOICES, default="Choose...")
    c2 = models.CharField(max_length=30, choices=CHOICES, default="Choose...")
    c3 = models.CharField(max_length=30, choices=CHOICES, default="Choose...")
    c4 = models.CharField(max_length=30, choices=CHOICES, default="Choose...")
    c5 = models.CharField(max_length=30, choices=CHOICES, default="Choose...")
    c6 = models.CharField(max_length=30, choices=CHOICES, default="Choose...")
    c7 = models.CharField(max_length=30, choices=CHOICES, default="Choose...")
    c8 = models.CharField(max_length=30, choices=CHOICES, default="Choose...")
    c9 = models.CharField(max_length=30, choices=CHOICES, default="Choose...")

    n1 = models.CharField(max_length=30, default="None", blank=True)
    n2 = models.CharField(max_length=30, default="None", blank=True)
    n3 = models.CharField(max_length=30, default="None", blank=True)
    n4 = models.CharField(max_length=30, default="None", blank=True)
    n5 = models.CharField(max_length=30, default="None", blank=True)
    n6 = models.CharField(max_length=30, default="None", blank=True)
    n7 = models.CharField(max_length=30, default="None", blank=True)
    n8 = models.CharField(max_length=30, default="None", blank=True)
    n9 = models.CharField(max_length=30, default="None", blank=True)

    o1 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(9)])
    o2 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(9)])
    o3 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(9)])
    o4 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(9)])
    o5 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(9)])
    o6 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(9)])
    o7 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(9)])
    o8 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(9)])
    o9 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(9)])

    rows = models.IntegerField(default=1, validators=[MinValueValidator(1)])

    def __str__(self):
        return self.name + ' (' + str(self.author) + ')' + ' (id ' + str(self.id) + ')'
