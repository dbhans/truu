from django.contrib import admin

# Register your models here.
from .models import Time
from .models import Semester
from .models import Schedule
from .models import Log
from .models import AdminComment

admin.site.register(Time)
admin.site.register(Semester)
admin.site.register(Schedule)
admin.site.register(Log)
admin.site.register(AdminComment)
