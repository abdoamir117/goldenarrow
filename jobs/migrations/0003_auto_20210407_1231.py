# Generated by Django 3.1.7 on 2021-04-07 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20210407_1228'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='close_at',
            new_name='closing_date',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='start_at',
            new_name='starting_date',
        ),
    ]
