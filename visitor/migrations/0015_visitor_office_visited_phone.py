# Generated by Django 4.1.5 on 2023-04-05 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitor', '0014_visitor_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitor',
            name='office_visited_phone',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]