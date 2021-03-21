# Generated by Django 3.1.7 on 2021-03-20 16:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0008_auto_20210320_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userapp',
            name='access_token_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 22, 16, 40, 24, 340470, tzinfo=utc), verbose_name='срок действия токена доступа'),
        ),
        migrations.AlterField(
            model_name='userapp',
            name='refresh_token_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 22, 16, 40, 24, 340519, tzinfo=utc), verbose_name='срок действия токена обновления'),
        ),
    ]