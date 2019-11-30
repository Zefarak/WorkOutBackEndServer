# Generated by Django 2.2.6 on 2019-11-28 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='workout',
            name='category',
            field=models.CharField(choices=[('a', 'AMRAP'), ('b', 'Rounds'), ('c', 'For Time'), ('d', 'Tabata')], default='a', max_length=1),
        ),
    ]
