# Generated by Django 4.1.3 on 2022-12-22 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_alter_healthdata_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='healthdata',
            name='height',
            field=models.IntegerField(default=180),
        ),
    ]
