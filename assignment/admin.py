from django.contrib import admin

from .models import Func, company, device, deviceLog, employee

# Register your models here.
admin.site.register(Func)
admin.site.register(company)
admin.site.register(employee)
admin.site.register(device)
admin.site.register(deviceLog)
