from django.contrib import admin
from .models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'category', 'date_reported')
    list_filter = ('status', 'category')
    search_fields = ('title', 'description', 'location')