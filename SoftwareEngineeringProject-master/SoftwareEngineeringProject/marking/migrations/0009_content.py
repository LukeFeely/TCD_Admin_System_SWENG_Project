# Generated by Django 2.0.3 on 2019-03-26 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marking', '0008_auto_20190324_1100'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('contentId', models.IntegerField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=10000)),
                ('weighted', models.BooleanField(default=True)),
                ('degreeId', models.IntegerField()),
                ('degreeName', models.CharField(max_length=200)),
                ('section', models.IntegerField()),
                ('year', models.IntegerField()),
            ],
        ),
    ]