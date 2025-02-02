# Generated by Django 4.2.10 on 2024-03-22 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mentalapp", "0008_resource_picture"),
    ]

    operations = [
        migrations.AddField(
            model_name="appointment",
            name="duration",
            field=models.IntegerField(default=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="post",
            name="title",
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
