# Generated by Django 2.1.5 on 2019-03-23 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marking', '0006_auto_20190318_1315'),
    ]

    operations = [
        migrations.CreateModel(
            name='ICSProjectModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('studentid', models.CharField(max_length=500)),
                ('supervisor', models.CharField(max_length=500)),
                ('date', models.CharField(max_length=500)),
                ('scopes_and_aims', models.CharField(max_length=500)),
                ('challenges', models.CharField(max_length=500)),
                ('problems_motivation_analysis', models.CharField(max_length=500)),
                ('problems_motivation_analysis_weighting', models.IntegerField()),
                ('problems_motivation_analysis_mark', models.IntegerField()),
                ('research_literature_review', models.CharField(max_length=500)),
                ('research_literature_review_analysis_weighting', models.IntegerField()),
                ('research_literature_review_analysis_mark', models.IntegerField()),
                ('technical_content_project_execution', models.CharField(max_length=500)),
                ('technical_content_project_execution_weighting', models.IntegerField()),
                ('technical_content_project_execution_mark', models.IntegerField()),
                ('testing_evaluation_analysis_conclusions', models.CharField(max_length=500)),
                ('testing_evaluation_analysis_conclusions_weighting', models.IntegerField()),
                ('testing_evaluation_analysis_conclusions_mark', models.IntegerField()),
                ('presentation_and_writing', models.CharField(max_length=500)),
                ('presentation_and_writing_weighting', models.IntegerField()),
                ('presentation_and_writing_mark', models.IntegerField()),
            ],
        ),
    ]