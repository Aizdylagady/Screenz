# Generated by Django 3.1 on 2021-03-03 08:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20210303_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='created',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
