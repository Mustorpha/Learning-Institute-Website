# Generated by Django 4.0 on 2021-12-24 21:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hosannaWebsite', '0015_rename_feature_image_course_featured_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='purchase_link',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.CreateModel(
            name='Outcome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('learning_outcomes', models.TextField(max_length=256)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hosannaWebsite.course')),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hosannaWebsite.course')),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson', models.CharField(max_length=256)),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hosannaWebsite.level')),
            ],
        ),
    ]