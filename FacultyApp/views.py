from django.shortcuts import render

from StudentApp.models import Students

# Create your views here.
def FacultyInterface(request):

    Student = Students.objects.all()

    context = {'Student':Student}
    return render(request,'faculty interface.html',context)