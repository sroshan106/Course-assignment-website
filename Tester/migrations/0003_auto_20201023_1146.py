# Generated by Django 2.2 on 2020-10-23 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tester', '0002_auto_20201023_1118'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='correct',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='questions',
            name='option1',
            field=models.TextField(default='YEAH', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='questions',
            name='option2',
            field=models.TextField(default='bLA', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='questions',
            name='option3',
            field=models.TextField(default='tHE', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='questions',
            name='option4',
            field=models.TextField(default='OUR', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='questions',
            name='slug',
            field=models.SlugField(default='QUESTION', unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='questions',
            name='wrong',
            field=models.BooleanField(default=False),
        ),
    ]
