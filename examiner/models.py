from django.db import models

# Create your models here.

class Results(models.Model):
    id = models.BigAutoField(primary_key=True)
    examid = models.ForeignKey('eadmin.Exam', on_delete=models.CASCADE) # models.CharField(max_length=10)
    reg_no = models.ForeignKey('home.Applicant', on_delete=models.CASCADE)
    grade = models.CharField(max_length=10)
    percentage = models.IntegerField(default=35)
    marks = models.IntegerField(default=35)

    class Meta:
        unique_together = (("examid", "reg_no"),)




# Create your models here.
class questions(models.Model):
    class Meta:
        unique_together = (('qid', 'examid'),)

    id = models.BigAutoField(primary_key=True)
    examid = models.CharField(max_length=15)
    qid = models.CharField(max_length=5, unique=True)
    q = models.TextField(unique=True)
    opta = models.TextField()
    optb = models.TextField()
    optc = models.TextField()
    optd = models.TextField()
    answer = models.TextField()





class responses(models.Model):
    class Meta:
        unique_together = (('studid', 'examid'))

    id = models.BigAutoField(primary_key=True)
    examid = models.CharField(max_length=5)
    studid = models.CharField(max_length=5)
    reponse = models.CharField(max_length=500)
    cor = models.CharField(max_length=2)
    wrg = models.CharField(max_length=2)
    una = models.CharField(max_length=2)
    total = models.CharField(max_length=5)
