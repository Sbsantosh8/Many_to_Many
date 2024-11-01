from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):

        return self.name


class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    students = models.ManyToManyField(Student, related_name="courses")

    def __str__(self):
        return self.title
