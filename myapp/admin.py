from django.contrib import admin
from .models import Profile

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'age',
        'address',
        'created_at',
        'image'
    ]
admin.site.register(Profile,ProfileAdmin)