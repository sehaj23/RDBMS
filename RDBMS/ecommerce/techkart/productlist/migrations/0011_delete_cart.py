# Generated by Django 2.2.3 on 2019-08-20 20:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productlist', '0010_remove_cart_p_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='cart',
        ),
    ]