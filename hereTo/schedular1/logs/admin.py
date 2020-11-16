from django.contrib import admin

# Register your models here.
from .models import Log
from .models import AdminComment

admin.site.register(Log)
admin.site.register(AdminComment)
