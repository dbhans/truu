from django.contrib import admin

# Register your models here.
from .models import Cours
from .models import Classroom
from .models import Programs
from .models import Softwares
from .models import Classroom_has_Softwares
from .models import Groups

admin.site.register(Cours)
admin.site.register(Classroom)
admin.site.register(Programs)
admin.site.register(Softwares)
admin.site.register(Classroom_has_Softwares)
admin.site.register(Groups)
