# Generated by Django 5.1.2 on 2024-10-24 17:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0003_grade_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grade',
            name='homework',
        ),
        migrations.AddField(
            model_name='homework',
            name='grade',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='homework.grade'),
        ),
    ]
