# Generated by Django 3.0.8 on 2020-09-01 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_auto_20200901_1559'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='date_updated',
        ),
        migrations.AlterField(
            model_name='project',
            name='project_image',
            field=models.URLField(),
        ),
    ]
