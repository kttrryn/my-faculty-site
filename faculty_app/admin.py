from django.contrib import admin

# Register your models here.
from .models import Department, Program, Teacher, MainPageInfo

admin.site.register(Department)
admin.site.register(Program)
admin.site.register(Teacher)
admin.site.register(MainPageInfo)
