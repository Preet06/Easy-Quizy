# Generated by Django 3.0.8 on 2021-06-19 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student_info',
            name='test_name',
        ),
    ]
