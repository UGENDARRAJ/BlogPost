# Generated by Django 4.2.9 on 2024-04-25 06:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='published_data',
            new_name='published_date',
        ),
    ]
