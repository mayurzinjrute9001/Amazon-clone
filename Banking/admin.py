from django.contrib import admin
from .models import User

class Admin_User(admin.ModelAdmin):
    list_display = ['name','email','phone','acc_number','acc_status']


admin.site.register(User,Admin_User)