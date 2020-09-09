from django.contrib import admin

from .models import Cpu, Company, Laptop


admin.site.register(Cpu)
admin.site.register(Company)
admin.site.register(Laptop)
