# Generated by Django 3.0.8 on 2020-08-10 07:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='realtor',
            old_name='hire_data',
            new_name='hire_date',
        ),
    ]
