# Generated by Django 5.1.2 on 2024-11-06 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_ordercourse_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='course',
            new_name='courses',
        ),
    ]