# Generated by Django 4.2 on 2023-04-20 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_items',
            field=models.ManyToManyField(through='core.OrderItem', to='core.product'),
        ),
    ]
