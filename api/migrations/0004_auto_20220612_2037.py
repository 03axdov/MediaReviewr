# Generated by Django 3.2 on 2022-06-12 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_userprofile_points'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='ranking',
            field=models.IntegerField(default=10000),
        ),
        migrations.AlterField(
            model_name='post',
            name='ranking2',
            field=models.IntegerField(default=10000),
        ),
        migrations.AlterField(
            model_name='post',
            name='ranking3',
            field=models.IntegerField(default=10000),
        ),
        migrations.AlterField(
            model_name='post',
            name='ranking4',
            field=models.IntegerField(default=10000),
        ),
    ]