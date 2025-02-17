# Generated by Django 4.2.1 on 2023-06-04 10:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myparking', '0009_alter_payment_receipt_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='client',
        ),
        migrations.AddField(
            model_name='account',
            name='user',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='account', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
