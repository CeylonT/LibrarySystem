# Generated by Django 2.2.7 on 2019-11-15 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='RoomType',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.RoomType'),
        ),
    ]
