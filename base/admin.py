from django.contrib import admin
from .models import User, School, NextOfKin, Payment
# Register your models here.

admin.site.register(User)
admin.site.register(School)
admin.site.register(NextOfKin)
admin.site.register(Payment)