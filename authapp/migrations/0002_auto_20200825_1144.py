# Generated by Django 3.0.8 on 2020-08-25 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='age',
            field=models.PositiveSmallIntegerField(blank=True, verbose_name='возраст'),
        ),
    ]
