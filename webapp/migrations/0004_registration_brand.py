# Generated by Django 3.2.7 on 2021-12-08 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_registration_hp'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='brand',
            field=models.CharField(default=0, max_length=250),
            preserve_default=False,
        ),
    ]
