from django.contrib import admin

# Register your models here.
from .models import Logs
from .models import AdminComments

admin.site.register(Logs)
admin.site.register(AdminComments)
