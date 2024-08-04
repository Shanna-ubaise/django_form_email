from django.contrib import admin
from .models import Complaint

@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'purchase_date', 'complaint_details', 'submitted_at')
    search_fields = ('product_name', 'complaint_details')
    list_filter = ('purchase_date', 'submitted_at')
