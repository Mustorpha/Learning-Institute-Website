# Generated by Django 4.0.3 on 2022-03-20 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosannaWebsite', '0045_tag_alter_course_date_added_news'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]