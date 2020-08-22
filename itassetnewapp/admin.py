from django.contrib import admin
from .models import Asset
from .forms import AssetForm
# Register your models here.


class AssetAdmin(admin.ModelAdmin):
    list_display = ['IP_address', 'hostname', 'business_name',
                    'hosting_location', 'db_make_model', 'webserver', 'primary_role', 'mobile_no', 'user_email', 'billingcount', 'source', 'severity', 'timestamp']
    form = AssetForm
    list_filter = ['IP_address', 'hostname', 'business_name',
                   'hosting_location', 'user_email', 'source', 'severity']
    search_fields = ['IP_address', 'hostname', 'business_name',
                     'hosting_location', 'user_email', 'source', 'severity']


admin.site.register(Asset, AssetAdmin)
