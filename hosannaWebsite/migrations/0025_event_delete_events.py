# Generated by Django 4.0 on 2022-03-08 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosannaWebsite', '0024_events_delete_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('short_note', models.TextField(max_length=300)),
                ('event_description', models.TextField(null=True)),
                ('featured_image', models.ImageField(default='default.jpg', upload_to='events')),
                ('topic', models.CharField(max_length=128)),
                ('host', models.CharField(max_length=128)),
                ('location', models.CharField(max_length=128)),
                ('skill_level', models.CharField(max_length=128)),
                ('language', models.CharField(max_length=128)),
                ('students', models.CharField(max_length=128)),
                ('date', models.DateField(null=True)),
                ('time', models.TimeField(null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Events',
        ),
    ]