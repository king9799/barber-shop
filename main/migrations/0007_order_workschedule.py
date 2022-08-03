# Generated by Django 3.2.9 on 2022-07-27 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20220727_1159'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_time', models.TimeField()),
                ('status', models.BooleanField(default=False)),
                ('date', models.DateField(auto_now_add=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('order_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=False)),
                ('date', models.DateField(auto_now_add=True)),
                ('bot_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.botuser')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.employee')),
            ],
        ),
    ]