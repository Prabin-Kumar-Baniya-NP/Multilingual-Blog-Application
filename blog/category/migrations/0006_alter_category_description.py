# Generated by Django 3.2.5 on 2021-09-02 16:20

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0005_auto_20210725_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, max_length=126, null=True, verbose_name='Category Description'),
        ),
    ]
