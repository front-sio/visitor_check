# Generated by Django 4.1.5 on 2023-04-06 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitor', '0016_visitor_sign_out_code_alter_visitor_time_in_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='sign_out_code',
            field=models.CharField(blank=True, max_length=6, null=True, unique=True),
        ),
    ]