# Generated by Django 3.0 on 2019-12-26 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20191226_1606'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='phone',
        ),
    ]
