# Generated by Django 3.2.16 on 2024-05-16 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20240515_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='', null=True, upload_to='posts/'),
        ),
    ]
