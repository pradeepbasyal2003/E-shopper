# Generated by Django 5.0.6 on 2024-12-11 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='checkout',
            field=models.BooleanField(default=False),
        ),
    ]
