# Generated by Django 2.0.3 on 2019-03-26 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marking', '0011_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='inputBox',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
    ]
