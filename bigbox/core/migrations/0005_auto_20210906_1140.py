# Generated by Django 3.2.1 on 2021-09-06 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20210906_1133'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='order',
            field=models.IntegerField(default=0, verbose_name='orden'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reason',
            name='order',
            field=models.IntegerField(default=0, verbose_name='orden'),
            preserve_default=False,
        ),
    ]