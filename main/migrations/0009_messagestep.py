# Generated by Django 3.2.9 on 2022-08-02 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_order_order_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageStep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step', models.IntegerField(default=0)),
            ],
        ),
    ]