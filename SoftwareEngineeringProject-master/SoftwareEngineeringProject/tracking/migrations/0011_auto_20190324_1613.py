# Generated by Django 2.1.7 on 2019-03-24 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0010_auto_20190324_1609'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='doingCompSciProject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='tracking.Project'),
        ),
        migrations.AlterField(
            model_name='project',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tracking.Student'),
        ),
    ]
