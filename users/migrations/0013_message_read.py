# Generated by Django 4.2.7 on 2024-05-08 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_message_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='read',
            field=models.BooleanField(default=False),
        ),
    ]