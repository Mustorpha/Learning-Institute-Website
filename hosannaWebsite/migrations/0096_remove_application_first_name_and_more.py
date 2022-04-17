# Generated by Django 4.0.3 on 2022-04-06 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosannaWebsite', '0095_remove_application_mode_of_payments_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='application',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='application',
            name='payment_status',
        ),
        migrations.AddField(
            model_name='application',
            name='full_name',
            field=models.CharField(default='', max_length=300),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='application',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=7),
        ),
        migrations.AlterField(
            model_name='application',
            name='title',
            field=models.CharField(choices=[('Mr', 'Mr'), ('Mrs', 'Mrs'), ('Miss', 'Miss'), ('Engr', 'Engr'), ('Dr', 'Dr')], default='Mr', max_length=5),
        ),
    ]
