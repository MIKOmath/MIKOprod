# Generated by Django 5.0.6 on 2024-06-20 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainSite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
