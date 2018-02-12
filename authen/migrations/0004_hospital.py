# Generated by Django 2.0.2 on 2018-02-10 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authen', '0003_profile_f3'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('time', models.CharField(max_length=150)),
                ('lat', models.CharField(max_length=100)),
                ('lng', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=300)),
                ('profile_pic', models.ImageField(blank=True, default='media/mainpage4.jpg', null=True, upload_to='')),
            ],
        ),
    ]