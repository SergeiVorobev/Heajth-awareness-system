# Generated by Django 4.1.3 on 2022-12-22 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suggestions', '0029_alter_questionarymodel_diet_meal_quantity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionarymodel',
            name='phisical_exercises',
            field=models.CharField(choices=[('Yes, and more then 2 hours per week', 'Yes More 2H Per Week'), ('Yes, but less then 2 hours per week', 'Yes Less 2H Per Week'), ('No, I do not do any physical exercises', 'No')], default='No, I do not do any phisical exercises', max_length=256),
        ),
    ]