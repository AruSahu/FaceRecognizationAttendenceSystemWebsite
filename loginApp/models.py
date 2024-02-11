from django.db import models


# Create your models here.

class LoginINFO(models.Model):
    loginID = models.CharField(max_length=60, default='')
    name = models.CharField(max_length=60, default='')
    password = models.CharField(max_length=60, default='')
    phoneNo = models.CharField(max_length=60, default='')
    isAdmin = models.BooleanField(default=False)

class AttendenceVideoUpload(models.Model):
    nameTeacher = models.CharField(max_length=255)
    semester = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    date = models.DateTimeField()
    videofile = models.FileField(upload_to="")

class AttendenceVideoFileUpload(models.Model):
    nameTeacher = models.CharField(max_length=255)
    semester = models.CharField(max_length=255)
    year = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    timing = models.CharField(max_length=255)
    videofile = models.FileField(upload_to="")

class AttendenceCSVFileUpload(models.Model):
    nameTeacher = models.CharField(max_length=255)
    semester_csv = models.CharField(max_length=255)
    year_csv = models.CharField(max_length=255)
    subject_csv = models.CharField(max_length=255)
    timing_csv = models.CharField(max_length=255)
    csvfile = models.FileField(upload_to="")