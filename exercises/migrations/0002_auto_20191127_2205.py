# Generated by Django 2.2 on 2019-11-27 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercisecategory',
            name='title',
            field=models.CharField(default='v', max_length=240, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='exercisecategory',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
