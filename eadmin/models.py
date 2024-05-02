from django.db import models
from datetime import date
import os

class Course(models.Model):
    id = models.BigAutoField(primary_key=True)
    coursecode = models.CharField(max_length=15, unique=True)
    coursename = models.CharField(max_length=40)
    examiner = models.ForeignKey('home.Examiner', on_delete=models.CASCADE)

class Exam(models.Model):
    id = models.BigAutoField(primary_key=True)
    examcode = models.CharField(max_length=40, unique=True)
    examname = models.CharField(max_length=40)
    examdate = models.DateField()
    course = models.ForeignKey('eadmin.Course', on_delete=models.CASCADE)
    examinerid = models.CharField(max_length=40, default='02')

def content_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s_%s.%s" % (instance.reg_no, 'paymentslip', ext)
    return os.path.join('documents/payment/', filename)

class Enrollments(models.Model):
    id = models.BigAutoField(primary_key=True)
    reg_no = models.ForeignKey('home.Applicant', on_delete=models.CASCADE)
    exam = models.ForeignKey('eadmin.Exam', on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    paymentref = models.FileField(upload_to=content_file_name)

    class Meta:
        unique_together = (("reg_no", "exam"),)
