from django.contrib import admin
from django.contrib.auth.models import Group
from .models import UserDash
from django.urls import path
from django.http import HttpResponseRedirect


class UserAdmin(admin.ModelAdmin):
    list_display = ('firstname' , 'created', 'font_size' )
    list_filter = ('created',)
    change_list_template = 'admin/user_dashboard/user_dashboard_change_list.html'

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('fontsize/<int:size>/', self.change_font_size)
        ]
        return custom_urls + urls

    def change_font_size(self, request, size):
        self.model.objects.all().update(font_size=size)
        self.message_user(request, 'font size set successfully!')
        return HttpResponseRedirect("../")
admin.site.site_header = 'EazzyCard'
admin.site.register(UserDash, UserAdmin)
admin.site.unregister(Group)
