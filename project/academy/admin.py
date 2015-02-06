from django.contrib import admin
from academy.models import Invite

class InviteAdmin(admin.ModelAdmin):
    list_display = ("name", "branch", "gender", "date_of_birth", "race")
    #list_filter = ("branch", "gender", "race")
    #search_fields = ("name",)
    #list_editable = ("gender", "date_of_birth", "race")

#admin.site.register(Invite)
admin.site.register(Invite, InviteAdmin)