# Generated by Django 5.2.2 on 2025-06-10 08:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0005_alter_notes_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2025, 6, 10, 18, 30, 13, 909307)),
        ),
    ]
