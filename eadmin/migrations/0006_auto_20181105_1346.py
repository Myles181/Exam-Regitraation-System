# Generated by Django 2.1.2 on 2018-11-05 08:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_applicant'),
        ('eadmin', '0005_auto_20181105_1340'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='enrollments',
            unique_together={('roll_no', 'examid')},
        ),
    ]