# Generated by Django 3.2.16 on 2023-10-20 06:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0008_auto_20231020_0900'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'default_related_name': 'comments', 'verbose_name': 'Комментарий', 'verbose_name_plural': 'Комментарии'},
        ),
        migrations.AlterModelOptions(
            name='follow',
            options={'verbose_name': 'Подписка', 'verbose_name_plural': 'Подписки'},
        ),
        migrations.AlterModelOptions(
            name='group',
            options={'verbose_name': 'Группа', 'verbose_name_plural': 'Группы'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'default_related_name': 'posts', 'ordering': ['pub_date'], 'verbose_name': 'Пост', 'verbose_name_plural': 'Посты'},
        ),
        migrations.AlterField(
            model_name='follow',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follower', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
