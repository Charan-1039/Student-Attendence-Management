from django.db import models

# Create your models here.
class Department(models.Model):
  BranchName= models.CharField(max_length=255)

def __str__(self) :
        return self.BranchName

class Subject(models.Model):
  SubjectName= models.CharField(max_length=255)

def __str__(self) :
        return self.SubjectName

class Class(models.Model):
  Class= models.CharField(max_length=255)

def __str__(self) :
        return self.Class

class Semester(models.Model):
  Semester= models.CharField(max_length=255)

def __str__(self) :
        return self.Semester


class StudentDatabase(models.Model):
     NAME=models.CharField(max_length=255)
     CLASS=models.CharField(max_length=255)
     SUB=models.CharField(max_length=255)
     SEM=models.CharField(max_length=255)
     USN=models.CharField(max_length=255)
     ATT=models.CharField(max_length=255)


     def __str__(self) :
        return self.NAME
