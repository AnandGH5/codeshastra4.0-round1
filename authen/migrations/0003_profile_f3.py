# Generated by Django 2.0.2 on 2018-02-10 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authen', '0002_auto_20180210_2327'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='f3',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
