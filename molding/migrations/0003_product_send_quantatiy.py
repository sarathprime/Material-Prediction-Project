# Generated by Django 4.0.2 on 2022-10-20 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('molding', '0002_product_send'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_send',
            name='quantatiy',
            field=models.CharField(default='exit', max_length=150),
            preserve_default=False,
        ),
    ]