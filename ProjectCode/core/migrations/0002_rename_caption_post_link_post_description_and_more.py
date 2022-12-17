# Generated by Django 4.1.2 on 2022-12-11 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='caption',
            new_name='Link',
        ),
        migrations.AddField(
            model_name='post',
            name='Description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='profile_images'),
        ),
    ]
