# Generated by Django 4.0.2 on 2022-10-13 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='send_mold',
            name='solutionss',
            field=models.CharField(default='exit', max_length=150),
            preserve_default=False,
        ),
    ]