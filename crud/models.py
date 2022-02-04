from django.db import models

# Create your models here.


class Student(models.Model):
    stu_roll = models.IntegerField()
    stu_name = models.CharField(max_length=70)
    stu_email = models.EmailField(max_length=70)
    stu_mobile = models.IntegerField()
    stu_image = models.ImageField()
