from django.contrib import admin
from .models.Fund import Fund

# Register your models here.


@admin.register(Fund)
class FundAdmin(admin.ModelAdmin):
    pass
