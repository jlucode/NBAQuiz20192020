# Generated by Django 3.0.4 on 2021-01-04 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0008_auto_20201221_2051'),
    ]

    operations = [
        migrations.AddField(
            model_name='scorer',
            name='condition_number',
            field=models.IntegerField(default=0),
        ),
    ]
