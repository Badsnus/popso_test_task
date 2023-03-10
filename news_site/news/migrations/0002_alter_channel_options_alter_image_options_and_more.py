# Generated by Django 4.1.7 on 2023-02-22 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='channel',
            options={'verbose_name': 'канал', 'verbose_name_plural': 'каналы'},
        ),
        migrations.AlterModelOptions(
            name='image',
            options={'verbose_name': 'изображение', 'verbose_name_plural': 'изображения'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'пост', 'verbose_name_plural': 'посты'},
        ),
        migrations.AddField(
            model_name='image',
            name='photo',
            field=models.ImageField(default='123123', upload_to='', verbose_name='фото'),
            preserve_default=False,
        ),
    ]
