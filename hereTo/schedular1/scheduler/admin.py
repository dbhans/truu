from django.contrib import admin

# Register your models here.
from .models import Time
from .models import Semesters
from .models import Schedule
from .models import Logs
from .models import AdminComments

admin.site.register(Time)
admin.site.register(Semesters)
admin.site.register(Schedule)
admin.site.register(Logs)
admin.site.register(AdminComments)
