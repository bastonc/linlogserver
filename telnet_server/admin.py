from django.contrib import admin
from .models import Chek_update, Register_new, Version,  Template, Admins

admin.site.register(Template)
admin.site.register(Chek_update)
admin.site.register(Register_new)
admin.site.register(Version)
admin.site.register(Admins)


# Register your models here.
