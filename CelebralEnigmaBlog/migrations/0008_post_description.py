# Generated by Django 5.0.6 on 2024-07-16 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CelebralEnigmaBlog', '0007_remove_post_time_post_date_alter_post_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.TextField(default=' ', max_length=600),
        ),
    ]
