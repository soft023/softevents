# Generated by Django 2.1.7 on 2019-03-28 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_booking_feedback'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='moreinfo',
            new_name='comment',
        ),
    ]
