# Generated by Django 2.2.8 on 2020-04-09 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogsite', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Blogsite',
            new_name='Blog',
        ),
    ]