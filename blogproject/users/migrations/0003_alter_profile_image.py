# Generated by Django 4.1 on 2022-08-19 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.jfif', upload_to='profile_pics'),
        ),
    ]
