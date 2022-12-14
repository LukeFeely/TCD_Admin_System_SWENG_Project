# Generated by Django 2.1.5 on 2019-04-10 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marking', '0020_icsprojectmodeldraft'),
    ]

    operations = [
        migrations.AlterField(
            model_name='icsprojectmodeldraft',
            name='presentation_and_writing_mark',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='icsprojectmodeldraft',
            name='presentation_and_writing_weighting',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='icsprojectmodeldraft',
            name='problems_motivation_analysis_mark',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='icsprojectmodeldraft',
            name='problems_motivation_analysis_weighting',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='icsprojectmodeldraft',
            name='research_literature_review_analysis_mark',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='icsprojectmodeldraft',
            name='research_literature_review_analysis_weighting',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='icsprojectmodeldraft',
            name='technical_content_project_execution_mark',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='icsprojectmodeldraft',
            name='technical_content_project_execution_weighting',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='icsprojectmodeldraft',
            name='testing_evaluation_analysis_conclusions_mark',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='icsprojectmodeldraft',
            name='testing_evaluation_analysis_conclusions_weighting',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
