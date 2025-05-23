# Generated by Django 4.2.16 on 2024-11-29 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ordermanagement', '0002_orders'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='amount',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='orders',
            name='bill_amount',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='orders',
            name='gst_amount',
            field=models.FloatField(default=0),
        ),
    ]
