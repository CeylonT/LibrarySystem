# Generated by Django 2.2.7 on 2019-11-14 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_librarian_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Penalty',
            fields=[
                ('PenaltyID', models.BigIntegerField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=20)),
                ('Point', models.IntegerField()),
            ],
        ),
    ]
