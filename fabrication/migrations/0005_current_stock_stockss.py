# Generated by Django 4.0.2 on 2022-10-26 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fabrication', '0004_alter_current_stock_queries'),
    ]

    operations = [
        migrations.AddField(
            model_name='current_stock',
            name='stockss',
            field=models.BooleanField(default=False),
        ),
    ]
