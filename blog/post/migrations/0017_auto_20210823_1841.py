# Generated by Django 3.2.5 on 2021-08-23 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0016_auto_20210725_1323'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(error_messages={'max_length': "Title cann't be more than 126 characters"}, max_length=126, verbose_name='Post Title'),
        ),
    ]