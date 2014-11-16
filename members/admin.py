from django.contrib import admin

# Register your models here.
from .models import \
    Member, Profile, Group, Email

class MemberAdmin(admin.ModelAdmin):
    list_display = ('user', 'status', 'last_activity')
    list_filter = [ 'status']

admin.site.register(Member, MemberAdmin)
admin.site.register(Profile)
admin.site.register(Group)
admin.site.register(Email)
