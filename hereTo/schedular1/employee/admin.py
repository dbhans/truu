from django.contrib import admin

# Register your models here.
from .models import Personnel
from .models import Availability
from .models import TeacherPreference

admin.site.register(Personnel)
admin.site.register(Availability)
admin.site.register(TeacherPreference)
