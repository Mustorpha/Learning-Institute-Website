# Generated by Django 4.0 on 2022-03-08 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosannaWebsite', '0027_alter_event_short_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='short_note',
            field=models.CharField(max_length=500),
        ),
    ]