# Generated by Django 3.0.6 on 2020-05-06 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0005_auto_20200506_1630'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='author',
            new_name='authors',
        ),
    ]
