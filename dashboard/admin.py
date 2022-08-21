from django.contrib import admin
from .models import *
from custom_user.admin import EmailUserAdmin
# Register your models here.

admin.site.register(Notes)
admin.site.register(Homework)
admin.site.register(Todo)


