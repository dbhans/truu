from django.contrib import admin

# Register your models here.
from .models import Cours
from .models import Classroom
from .models import Programs
from .models import Softwares
from .models import Groups

admin.site.register(Cours)