# Generated by Django 3.1.3 on 2021-01-07 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zoos', '0004_zoo_street'),
    ]

    operations = [
        migrations.AddField(
            model_name='zoo',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='zoo',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
