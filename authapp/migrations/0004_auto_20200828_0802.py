# Generated by Django 3.0.8 on 2020-08-28 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0003_auto_20200825_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='age',
            field=models.PositiveSmallIntegerField(verbose_name='возраст'),
        ),
    ]
