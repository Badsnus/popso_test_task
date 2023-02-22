# Generated by Django 4.1.7 on 2023-02-22 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_channel_options_alter_image_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='name',
            field=models.CharField(max_length=50, verbose_name='название'),
        ),
        migrations.AlterField(
            model_name='image',
            name='photo',
            field=models.ImageField(upload_to='media/', verbose_name='фото'),
        ),
    ]