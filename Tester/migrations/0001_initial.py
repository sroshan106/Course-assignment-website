# Generated by Django 2.2 on 2020-10-23 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ques', models.TextField(max_length=1000)),
                ('answer', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Examinations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questions', models.ManyToManyField(to='Tester.Questions')),
            ],
        ),
    ]
