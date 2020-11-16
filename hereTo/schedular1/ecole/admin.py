from django.contrib import admin

# Register your models here.
from .models import Cour
from .models import Classroom
from .models import Program
from .models import Software
from .models import Classroom_has_Software
from .models import Group

admin.site.register(Cour)
Cour.objects.all()
admin.site.register(Classroom)
admin.site.register(Program)
admin.site.register(Software)
admin.site.register(Classroom_has_Software)
admin.site.register(Group)
