# Generated by Django 2.0.5 on 2018-06-02 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaf', '0002_auto_20180513_2356'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cafe',
            name='tag_id',
        ),
        migrations.AddField(
            model_name='cafe',
            name='tags',
            field=models.ManyToManyField(to='leaf.Tag'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
