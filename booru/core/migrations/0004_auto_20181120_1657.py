# Generated by Django 2.1.2 on 2018-11-20 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20181120_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bannedhash',
            name='content',
            field=models.CharField(max_length=32),
        ),
    ]
