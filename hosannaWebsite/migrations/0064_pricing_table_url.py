# Generated by Django 4.0.3 on 2022-03-29 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosannaWebsite', '0063_alter_course_certification_alter_course_popular'),
    ]

    operations = [
        migrations.AddField(
            model_name='pricing_table',
            name='url',
            field=models.CharField(max_length=500, null=True),
        ),
    ]