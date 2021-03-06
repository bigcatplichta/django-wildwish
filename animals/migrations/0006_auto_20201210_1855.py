# Generated by Django 3.1.3 on 2020-12-11 01:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_image_title'),
        ('animals', '0005_auto_20201202_2126'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='recent_img',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='recent_img', to='images.image'),
        ),
        migrations.AlterField(
            model_name='donation',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='animals.user'),
        ),
    ]
