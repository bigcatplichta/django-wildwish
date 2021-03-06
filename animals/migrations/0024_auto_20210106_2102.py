# Generated by Django 3.1.3 on 2021-01-07 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0023_auto_20210106_1949'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='animal',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='animal',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
