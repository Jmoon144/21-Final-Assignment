# Generated by Django 3.2.5 on 2021-07-19 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='number',
            field=models.CharField(default=1, max_length=4),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='admin',
            name='password',
            field=models.CharField(max_length=4),
        ),
    ]
