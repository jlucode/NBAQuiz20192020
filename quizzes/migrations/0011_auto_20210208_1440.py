# Generated by Django 3.0.4 on 2021-02-08 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0010_auto_20210202_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scorer',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
