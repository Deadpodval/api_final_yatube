# Generated by Django 3.2.16 on 2024-05-17 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_alter_follow_following'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follow',
            name='following',
            field=models.SlugField(max_length=256),
        ),
    ]
