# Generated by Django 4.0.5 on 2022-06-14 00:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_deleteditem'),
    ]

    operations = [
        migrations.AddField(
            model_name='deleteditem',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
