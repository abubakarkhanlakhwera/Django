from django.contrib import admin
from .models import HRProfile

class HRProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'company_name', 'position_title', 'contact_number', 'email')
    search_fields = ('full_name', 'company_name', 'position_title', 'contact_number', 'email')
    list_filter = ('company_name', 'position_title')
    ordering = ('-user',)  # Assuming 'user' is a relevant field for ordering

    def get_readonly_fields(self, request, obj=None):
        if obj:  # Editing an existing object
            return ('user',)  # Example: Make the 'user' field read-only
        else:  # Creating a new object
            return ()

    def save_model(self, request, obj, form, change):
        if not obj.pk:  # If it's a new object
            obj.user = request.user  # Set the user to the currently logged-in user
        super().save_model(request, obj, form, change)

admin.site.register(HRProfile, HRProfileAdmin)
