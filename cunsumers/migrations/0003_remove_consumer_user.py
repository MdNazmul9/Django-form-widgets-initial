# Generated by Django 3.1.1 on 2021-03-10 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cunsumers', '0002_consumer_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consumer',
            name='user',
        ),
    ]
