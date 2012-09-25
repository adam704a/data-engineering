from dataloader.models import Merchant,Item,Purchaser,Order
from django.contrib import admin

class PollAdmin(admin.ModelAdmin):
    fields = ['name', 'address']

admin.site.register(Merchant, PollAdmin)
