# Generated by Django 4.2.4 on 2023-08-03 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appTelovendo', '0002_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='login',
            name='password',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='login',
            name='username',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
