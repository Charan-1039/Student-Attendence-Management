from django.contrib import admin
from DetailsApp.models import Department,Subject,Semester,StudentDatabase

# Register your models here.






class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('BranchName',)  # Fields to display in the list view

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('SubjectName',)  # Fields to display in the list view

class SemAdmin(admin.ModelAdmin):
    list_display = ('Semester',)  # Fields to display in the list view
   


admin.site.register(Department,DepartmentAdmin)
admin.site.register(Subject,SubjectAdmin)

admin.site.register(Semester,SemAdmin)

admin.site.register(StudentDatabase)