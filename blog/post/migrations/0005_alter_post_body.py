# Generated by Django 3.2.3 on 2021-06-22 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(default='None', max_length=1000),
        ),
    ]
