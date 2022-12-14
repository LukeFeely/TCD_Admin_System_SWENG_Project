# Generated by Django 2.1.7 on 2019-03-18 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0004_auto_20190318_2041'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='supervisor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='tracking.Supervisor'),
        ),
        migrations.AddIndex(
            model_name='project',
            index=models.Index(fields=['supervisor'], name='tracking_pr_supervi_1b6615_idx'),
        ),
    ]
