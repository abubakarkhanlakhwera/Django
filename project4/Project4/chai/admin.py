from django.contrib import admin
from . import models
class ChaiReviewInline(admin.TabularInline):
    model = models.ChaiReview
    extra = 2
class ChaiVarietyAdmin(admin.ModelAdmin):
    list_display = ('name','type','date_added',)
    inlines = [ChaiReviewInline]
    
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name','location',)
    filter_horizontal = ('chai_varaities',)
class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display = ('chai','certificate_number',)
    

admin.site.register(models.ChaiVariety,ChaiVarietyAdmin)
# admin.site.register(models.ChaiReview,ChaiReviewInline)
admin.site.register(models.ChaiCertificate,ChaiCertificateAdmin)
admin.site.register(models.Store,StoreAdmin)
