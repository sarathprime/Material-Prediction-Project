# Generated by Django 4.0.2 on 2022-10-26 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consumer', '0005_requirement_materails'),
    ]

    operations = [
        migrations.AddField(
            model_name='requirement',
            name='b2',
            field=models.BooleanField(default=False),
        ),
    ]
