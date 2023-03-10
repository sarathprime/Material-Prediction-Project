# Generated by Django 4.0.2 on 2022-10-14 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='molding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=150, unique=True)),
                ('password', models.CharField(max_length=150)),
                ('phonenumber', models.PositiveBigIntegerField(null=True)),
                ('gender', models.CharField(max_length=150, null=True)),
                ('address', models.CharField(max_length=150, null=True)),
                ('actions', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=150)),
                ('computer', models.CharField(max_length=150)),
                ('electronics', models.CharField(max_length=150)),
                ('ceramics', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='team_register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Team', models.CharField(max_length=150)),
                ('Email', models.CharField(max_length=150)),
            ],
        ),
    ]
