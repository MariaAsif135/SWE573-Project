# Generated by Django 4.1.2 on 2022-12-19 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_post_image_alter_post_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Link',
            field=models.TextField(),
        ),
    ]
