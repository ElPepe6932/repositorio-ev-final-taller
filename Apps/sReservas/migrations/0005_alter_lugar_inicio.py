# Generated by Django 4.1.3 on 2022-12-20 19:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sReservas', '0004_alter_lugar_inicio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lugar',
            name='inicio',
            field=models.DateTimeField(auto_created=True, default=django.utils.timezone.now),
        ),
    ]
