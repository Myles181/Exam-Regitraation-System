# Generated by Django 2.1.2 on 2018-11-22 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examiner', '0008_results'),
    ]

    operations = [
        migrations.AddField(
            model_name='results',
            name='marks',
            field=models.IntegerField(default=35),
        ),
        migrations.AddField(
            model_name='results',
            name='percentage',
            field=models.IntegerField(default=35),
        ),
    ]