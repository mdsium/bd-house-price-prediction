from django.contrib import admin
from .models import ContactMessage, HousePrediction

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at', 'is_read']
    list_filter = ['is_read', 'created_at']
    search_fields = ['name', 'email', 'subject', 'message']
    readonly_fields = ['created_at']
    
    # Make it easy to mark as read
    actions = ['mark_as_read']

    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
    mark_as_read.short_description = "Mark selected messages as Read"




@admin.register(HousePrediction)
class HousePredictionAdmin(admin.ModelAdmin):
    list_display = ['created_at', 'city', 'thana', 'area_sqft', 'bedrooms', 'predicted_price', 'formatted_price']
    list_filter = ['city', 'created_at']
    search_fields = ['city', 'thana', 'name', 'email']
    readonly_fields = ['created_at', 'predicted_price', 'formatted_price']
    date_hierarchy = 'created_at'