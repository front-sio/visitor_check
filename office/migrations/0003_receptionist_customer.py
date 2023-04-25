# Generated by Django 4.1.5 on 2023-04-13 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_delete_receptionist'),
        ('office', '0002_receptionist'),
    ]

    operations = [
        migrations.AddField(
            model_name='receptionist',
            name='customer',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='customer.customer'),
        ),
    ]
