# Generated by Django 4.2.10 on 2024-03-09 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mentalapp", "0003_delete_profile"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="first_name",
            field=models.TextField(default="Dema", verbose_name="first name"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="customuser",
            name="last_name",
            field=models.TextField(default="Izere", verbose_name="last name"),
            preserve_default=False,
        ),
    ]
