# Generated by Django 4.0 on 2024-05-20 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='like_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='post_image',
            field=models.ImageField(default='null', upload_to='upload/post_images'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='view_status',
            field=models.BooleanField(default=False),
        ),
    ]
