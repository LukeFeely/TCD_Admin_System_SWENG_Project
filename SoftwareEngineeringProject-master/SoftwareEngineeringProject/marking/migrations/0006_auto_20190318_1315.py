# Generated by Django 2.1.5 on 2019-03-18 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marking', '0005_project_alloweddifferenceinmarks'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='readerOneHasDraft',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='project',
            name='readerTWoHasDraft',
            field=models.BooleanField(default=False),
        ),
    ]