from django.db import models
from DetailsApp.models import Department,Semester

# Create your models here.
class Students(models.Model):
  StudentName= models.CharField(max_length=255)
  USN=models.CharField(max_length=255)
  Sem=models.ForeignKey(Semester,on_delete=models.CASCADE ,null=True)
  Department=models.ForeignKey(Department,on_delete=models.CASCADE ,null=True)

def __str__(self) :
        return self.StudentName



































































































































































































































































