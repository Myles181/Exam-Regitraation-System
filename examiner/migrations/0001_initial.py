# Generated by Django 2.1.2 on 2018-11-04 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0008_applicant'),
        ('eadmin', '0003_enrollments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(max_length=10)),
                ('examid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eadmin.Exam')),
                ('roll_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Applicant')),
            ],
        ),
    ]