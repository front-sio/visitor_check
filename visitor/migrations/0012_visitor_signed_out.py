# Generated by Django 4.1.5 on 2023-04-04 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitor', '0011_alter_visitor_time_in_alter_visitor_time_out'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitor',
            name='signed_out',
            field=models.BooleanField(default=0, null=True),
        ),
    ]