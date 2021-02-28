# Generated by Django 3.1 on 2021-02-28 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0004_auto_20210228_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='budget',
            field=models.PositiveBigIntegerField(default=0, help_text='specify the amount in dollars'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='gross_in_the_world',
            field=models.PositiveBigIntegerField(default=0, help_text='specify the amount in dollars'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='gross_in_usa',
            field=models.PositiveBigIntegerField(default=0, help_text='specify the amount in dollars'),
        ),
    ]
