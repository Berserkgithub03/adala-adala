# Generated by Django 4.2.7 on 2024-05-10 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_remove_message_read'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriptionplan',
            name='duration',
            field=models.CharField(choices=[('3_minutes', '3 Minutes'), ('1_year', '1 Year'), ('lifetime', 'Lifetime')], max_length=50, null=True),
        ),
    ]
