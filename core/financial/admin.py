from django.contrib import admin
from .models import Financial, OfficeExpenses, Coupon

# Register your models here.
admin.site.register(Financial)
admin.site.register(OfficeExpenses)
admin.site.register(Coupon)
