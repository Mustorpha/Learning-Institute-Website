# Generated by Django 4.0.3 on 2022-04-06 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosannaWebsite', '0091_alter_application_payment_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='payment_status',
            field=models.CharField(choices=[(True, 'Paid'), (False, 'Waiting')], default=False, max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='title',
            field=models.CharField(choices=[('Mr', 'Mr'), ('Mrs', 'Mrs'), ('Miss', 'Miss'), ('Engr', 'Engr'), ('Dr', 'Dr')], default='Mr', max_length=5),
        ),
    ]
