# Generated by Django 5.1.2 on 2024-10-18 18:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_order_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordercourse',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_courses', to='orders.order'),
        ),
    ]