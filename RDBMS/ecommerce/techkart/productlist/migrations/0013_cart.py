# Generated by Django 2.2.3 on 2019-08-23 19:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('productlist', '0012_auto_20190823_1554'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('cid', models.AutoField(max_length=10, primary_key=True, serialize=False)),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productlist.listing')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]