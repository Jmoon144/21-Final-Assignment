# Generated by Django 3.2.5 on 2021-07-19 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publics', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='public',
            name='number',
            field=models.CharField(default=1, max_length=4),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='public',
            name='password',
            field=models.CharField(max_length=4),
        ),
    ]
