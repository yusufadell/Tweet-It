# Generated by Django 3.2.13 on 2022-06-06 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0003_alter_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(default='default.png', upload_to='users/%Y/%m/%d/'),
        ),
    ]
