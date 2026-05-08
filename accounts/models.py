from django.db import models

# Create your models here.
from django.db import models

class ITI(models.Model):
    academic = models.CharField(max_length=100)
    specialization = models.TextField()

    def __str__(self):
        return f"{self.academic} - {self.specialization}"


class UG_Courses(models.Model):
    academic = models.CharField(max_length=100)
    specialization = models.TextField()

    def __str__(self):
        return f"{self.academic} - {self.specialization}"


class PG_Courses(models.Model):
    academic = models.CharField(max_length=100)
    specialization = models.TextField()

    def __str__(self):
        return f"{self.academic} - {self.specialization}"


class Intermediate_Courses(models.Model):
    academic = models.CharField(max_length=100)
    specialization = models.TextField()

    def __str__(self):
        return f"{self.academic} - {self.specialization}"


class Vocational_Courses(models.Model):
    academic = models.CharField(max_length=100)
    specialization = models.TextField()

    def __str__(self):
        return f"{self.academic} - {self.specialization}"
    


class Degree(models.Model):
    academic = models.CharField(max_length=100)
    specialization = models.TextField()
    sub_course = models.TextField()

    def __str__(self):
        return f"{self.academic} - {self.specialization} - {self.sub_course}"
    

class Polytechnic(models.Model):
    academic = models.CharField(max_length=100)
    specialization = models.TextField()

    def __str__(self):
        return f"{self.academic} - {self.specialization}"