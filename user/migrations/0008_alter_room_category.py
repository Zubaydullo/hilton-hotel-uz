# Generated by Django 3.2.5 on 2021-07-27 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_alter_room_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='room_category', to='user.roomcategory'),
        ),
    ]
