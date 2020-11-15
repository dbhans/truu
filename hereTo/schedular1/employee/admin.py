from django.contrib import admin

# Register your models here.
from .models import Personnels
from .models import Availability
from .models import TeacherPreferences

admin.site.register(Personnels)
admin.site.register(Availability)
admin.site.register(TeacherPreferences)
