# Generated by Django 4.2 on 2023-04-20 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_order_order_items'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='status',
        ),
    ]
