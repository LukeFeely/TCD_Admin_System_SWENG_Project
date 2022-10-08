# Generated by Django 2.1.5 on 2019-04-10 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marking', '0019_auto_20190409_1238'),
    ]

    operations = [
        migrations.CreateModel(
            name='ICSProjectModelDraft',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=500)),
                ('studentid', models.CharField(blank=True, max_length=500)),
                ('supervisor', models.CharField(blank=True, max_length=500)),
                ('date', models.CharField(blank=True, max_length=500)),
                ('scopes_and_aims', models.CharField(blank=True, max_length=500)),
                ('challenges', models.CharField(blank=True, max_length=500)),
                ('problems_motivation_analysis', models.CharField(blank=True, max_length=500)),
                ('problems_motivation_analysis_weighting', models.IntegerField(blank=True)),
                ('problems_motivation_analysis_mark', models.IntegerField(blank=True)),
                ('research_literature_review', models.CharField(blank=True, max_length=500)),
                ('research_literature_review_analysis_weighting', models.IntegerField(blank=True)),
                ('research_literature_review_analysis_mark', models.IntegerField(blank=True)),
                ('technical_content_project_execution', models.CharField(blank=True, max_length=500)),
                ('technical_content_project_execution_weighting', models.IntegerField(blank=True)),
                ('technical_content_project_execution_mark', models.IntegerField(blank=True)),
                ('testing_evaluation_analysis_conclusions', models.CharField(blank=True, max_length=500)),
                ('testing_evaluation_analysis_conclusions_weighting', models.IntegerField(blank=True)),
                ('testing_evaluation_analysis_conclusions_mark', models.IntegerField(blank=True)),
                ('presentation_and_writing', models.CharField(blank=True, max_length=500)),
                ('presentation_and_writing_weighting', models.IntegerField(blank=True)),
                ('presentation_and_writing_mark', models.IntegerField(blank=True)),
            ],
        ),
    ]