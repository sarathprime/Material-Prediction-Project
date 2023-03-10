# Generated by Django 4.0.2 on 2022-10-12 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consumer', '0002_rename_fabrication_consumer'),
    ]

    operations = [
        migrations.CreateModel(
            name='company_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=150, unique=True)),
                ('city', models.CharField(max_length=150)),
                ('state', models.CharField(max_length=150, null=True)),
                ('pincode', models.CharField(max_length=150, null=True)),
                ('country', models.CharField(max_length=150, null=True)),
                ('message', models.CharField(max_length=150, null=True)),
            ],
        ),
    ]
