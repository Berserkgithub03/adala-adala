# Generated by Django 4.2.7 on 2024-05-18 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0023_rename_document_documents'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notaryclient',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='notaryclient',
            name='mobile',
            field=models.IntegerField(null=True),
        ),
    ]