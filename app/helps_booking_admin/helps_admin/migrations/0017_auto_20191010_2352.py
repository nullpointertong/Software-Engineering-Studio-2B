# Generated by Django 2.2.4 on 2019-10-10 12:52

from django.db import migrations, models
import helps_admin.models


class Migration(migrations.Migration):

    dependencies = [
        ('helps_admin', '0016_auto_20191010_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffaccount',
            name='DOB',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='staffaccount',
            name='session_history',
            field=helps_admin.models.DateListField(),
        ),
    ]
