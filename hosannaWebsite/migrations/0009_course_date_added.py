# Generated by Django 4.0 on 2021-12-15 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosannaWebsite', '0008_alter_course_is_popular'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='date_added',
            field=models.DateTimeField(null=True),
        ),
    ]