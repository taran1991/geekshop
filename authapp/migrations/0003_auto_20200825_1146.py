# Generated by Django 3.0.8 on 2020-08-25 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_auto_20200825_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='age',
            field=models.PositiveSmallIntegerField(default=21, verbose_name='возраст'),
        ),
    ]