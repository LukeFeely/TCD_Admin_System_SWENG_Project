# Generated by Django 2.1.7 on 2019-03-24 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0014_project_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='student',
        ),
    ]
