# Generated by Django 2.2.7 on 2019-12-11 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plannerworkout',
            name='date_done',
            field=models.DateField(blank=True, null=True),
        ),
    ]
