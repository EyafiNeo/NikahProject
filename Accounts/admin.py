from django.contrib import admin
from Accounts.models import UserProfile, profileInfo, matching

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(profileInfo)
admin.site.register(matching)