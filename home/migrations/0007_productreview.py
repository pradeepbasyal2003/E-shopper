# Generated by Django 5.0.6 on 2024-12-16 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_cart_checkout'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=300)),
                ('slug', models.CharField(max_length=300)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('star', models.IntegerField()),
                ('comment', models.TextField()),
            ],
        ),
    ]
