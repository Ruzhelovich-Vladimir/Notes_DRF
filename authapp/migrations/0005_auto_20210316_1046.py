# Generated by Django 3.1.7 on 2021-03-16 10:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0004_auto_20210316_0502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userapp',
            name='access_token_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 18, 10, 46, 53, 45601, tzinfo=utc), verbose_name='срок действия токена доступа'),
        ),
        migrations.AlterField(
            model_name='userapp',
            name='refresh_token_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 18, 10, 46, 53, 45649, tzinfo=utc), verbose_name='срок действия токена обновления'),
        ),
    ]
