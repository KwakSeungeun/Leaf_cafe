# Generated by Django 2.0.5 on 2018-06-06 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leaf', '0005_auto_20180606_1502'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='cafe_id',
            new_name='cafe',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='user_id',
            new_name='email',
        ),
    ]