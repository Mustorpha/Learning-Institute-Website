# Generated by Django 4.0.3 on 2022-03-26 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosannaWebsite', '0061_course_course_description_course_duration_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='certification',
            field=models.IntegerField(choices=[(1, 'Yes'), (0, 'No')], null=True),
        ),
    ]