# Generated by Django 3.2.16 on 2023-10-18 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20231018_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follow',
            name='following',
            field=models.CharField(max_length=20, verbose_name='Объект подписки'),
        ),
    ]
