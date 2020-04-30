# Generated by Django 2.1.2 on 2019-03-03 02:27

from django.db import migrations, models

class Migration(migrations.Migration):

  initial = True

  dependencies = [
  ]

  operations = [
    migrations.CreateModel(
      name='Cat',
      fields=[
        ('id', models.AutoField(auto_created=True,
                                primary_key=True, serialize=False, verbose_name='ID')),
        ('name', models.CharField(max_length=100)),
        ('breed', models.CharField(max_length=100)),
        ('description', models.TextField(max_length=250)),
        ('age', models.IntegerField()),
      ],
    ),
  ]
