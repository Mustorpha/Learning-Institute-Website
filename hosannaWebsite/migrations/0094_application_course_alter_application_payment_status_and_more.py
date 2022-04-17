# Generated by Django 4.0.3 on 2022-04-06 21:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hosannaWebsite', '0093_alter_application_payment_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hosannaWebsite.course'),
        ),
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
