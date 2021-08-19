from django.db import models
from PIL import Image
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField


class Company(models.Model):
    name_company = models.CharField(max_length=200, null=True)
    full_name = models.CharField(max_length=200)
    description = RichTextUploadingField(max_length=5000)
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    address = models.CharField(max_length=200)

    class Meta:
        ordering = ['name_company']

    def get_absolute_url(self):
        return reverse('company-detail', args=[str(self.pk)])

    def __str__(self):
        return self.name_company

class Manager(models.Model):
    name_company = models.ForeignKey('Company', on_delete=models.SET_NULL, null=True)
    name_manager = models.CharField(max_length=200)

    def __str__(self):
        return self.name_manager

class ContactPhones(models.Model):
    name_company = models.ForeignKey('Company', on_delete=models.SET_NULL, null=True)
    phone = models.CharField(max_length=10, unique=True)
    name_manager = models.ForeignKey('Manager', on_delete=models.SET_NULL, null=True)
    STATUS = (
        ('d', 'Director'),
        ('m', 'Manager')
    )
    status = models.CharField(max_length=1, choices=STATUS, blank=True)

    def __str__(self):
        return f'{self.name_manager} - ({self.phone})'

class ContactEmail(models.Model):
    name_company = models.ForeignKey('Company', on_delete=models.SET_NULL, null=True)
    email = models.EmailField(unique=True)
    STATUS = (
        ('d', 'Director'),
        ('m', 'Manager')
    )
    name_manager = models.ForeignKey('Manager', on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=1, choices=STATUS, blank=True)

    def __str__(self):
        return f'{self.name_manager} - ({self.email})'

class Project(models.Model):
    company = models.ForeignKey('Company', on_delete=models.SET_NULL, null=True)
    name_project = models.CharField(max_length=100)
    project_description = RichTextUploadingField(max_length=5000)
    start_date = models.DateField()
    deadline = models.DateField()
    price = models.CharField(max_length=100)

    def __str__(self):
        return self.name_project

    def get_absolute_url(self):
        return reverse('project-detail', args=[str(self.pk)])

class Connection(models.Model):
    name_project = models.ForeignKey('Project', on_delete=models.SET_NULL, null=True)
    REFERENCES = (
        ('l', 'letter'),
        ('c', 'call')
    )
    reference = models.CharField(max_length=1, choices=REFERENCES, blank=True)
    descrip_connection = RichTextUploadingField(max_length=5000)
    MARKS = (
        ('l', 'like'),
        ('d', 'dislike')
    )
    mark = models.CharField(max_length=1, choices=MARKS, blank=True)
    user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)

    def get_absolute_url(self):
        return reverse('connect-detail', args=[str(self.pk)])

    def __str__(self):
        return f'{self.name_project}'

class User(AbstractUser):
    photo = models.ImageField(upload_to='images/', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('user-detail', args=[str(self.pk)])