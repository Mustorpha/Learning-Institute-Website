# Generated by Django 4.0.3 on 2022-03-19 22:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hosannaWebsite', '0041_system'),
    ]

    operations = [
        migrations.RenameField(
            model_name='system',
            old_name='Author',
            new_name='author',
        ),
    ]