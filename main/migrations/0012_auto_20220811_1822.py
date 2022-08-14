# Generated by Django 3.2.9 on 2022-08-11 22:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_botuser_language'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workschedule',
            name='order_time',
        ),
        migrations.AddField(
            model_name='workschedule',
            name='end',
            field=models.CharField(default=django.utils.timezone.now, max_length=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workschedule',
            name='start',
            field=models.CharField(default=django.utils.timezone.now, max_length=12),
            preserve_default=False,
        ),
    ]
