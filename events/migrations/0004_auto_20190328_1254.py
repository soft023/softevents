# Generated by Django 2.1.7 on 2019-03-28 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20190328_1253'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='Addedby',
            new_name='addedby',
        ),
    ]
