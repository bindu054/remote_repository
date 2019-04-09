from django.contrib import admin

# Register your models here.
from appgym.models import Registration
from appgym.models import Password

admin.site.register(Registration)
admin.site.register(Password)
