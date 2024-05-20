# Generated by Django 4.2.11 on 2024-05-20 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0013_alter_jobs_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Укажите зарплату в BYN', max_digits=6, null=True),
        ),
    ]
