# Generated by Django 3.2.3 on 2021-06-27 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0004_auto_20210622_2019'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='downvote',
            new_name='dislikes',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='upvote',
            new_name='likes',
        ),
    ]
