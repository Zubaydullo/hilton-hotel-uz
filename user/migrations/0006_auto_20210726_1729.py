# Generated by Django 3.2.5 on 2021-07-26 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20210726_1634'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roomcategory',
            name='price',
        ),
        migrations.AddField(
            model_name='room',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
