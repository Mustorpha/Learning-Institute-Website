# Generated by Django 4.0 on 2022-03-08 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosannaWebsite', '0020_remove_event_host_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='featured_image',
            field=models.ImageField(default='default.jpg', upload_to='events'),
        ),
    ]