# Generated by Django 3.2.18 on 2023-04-15 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LittleLemonAPI', '0007_alter_cart_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
    ]
