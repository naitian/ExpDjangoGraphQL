# Generated by Django 3.0.6 on 2020-05-06 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0006_auto_20200506_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='authors',
            field=models.ManyToManyField(related_name='posts', to='stories.Author'),
        ),
    ]
