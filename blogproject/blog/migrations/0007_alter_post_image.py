# Generated by Django 4.1 on 2022-09-04 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='blog_images/default.jfif', upload_to='blog_images'),
        ),
    ]
