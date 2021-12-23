from django.contrib import admin
from academy.models import Invite

class InviteAdmin(admin.ModelAdmin):
  list_display = ("name", "branch", "gender", "date_of_birth", "race", "reporter",)
  list_filter = ("branch", "gender", "race", "reporter",)
  list_editable = ("reporter",)
  search_fields = ("name",)

admin.site.register(Invite, InviteAdmin)
