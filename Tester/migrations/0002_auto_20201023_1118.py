# Generated by Django 2.2 on 2020-10-23 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tester', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='examinations',
            name='Name',
            field=models.CharField(default='HTFC', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='examinations',
            name='slug',
            field=models.SlugField(default='Examination-1', unique=True),
            preserve_default=False,
        ),
    ]
