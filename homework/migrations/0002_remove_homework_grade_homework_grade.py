# Generated by Django 5.1.2 on 2024-10-27 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homework',
            name='grade',
        ),
        migrations.AddField(
            model_name='homework',
            name='grade',
            field=models.ManyToManyField(to='homework.grade'),
        ),
    ]
