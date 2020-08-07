from django.contrib import admin
from .models import Chek_update, Register_new, Version,  Template, Admins

admin.site.register(Template)
#admin.site.register(Chek_update)
admin.site.register(Register_new)
admin.site.register(Version)
admin.site.register(Admins)
@admin.register(Chek_update)
class Chek_updateAdmin(admin.ModelAdmin):
    list_display = ('call', 'version', 'timestamp')
    search_fields = ('call', 'version')
    class Meta:
        ordering = ("-timestamp")


# Register your models here.
