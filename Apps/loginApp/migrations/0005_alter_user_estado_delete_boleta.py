# Generated by Django 4.1 on 2022-12-21 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginApp', '0004_alter_user_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='estado',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.DeleteModel(
            name='Boleta',
        ),
    ]
