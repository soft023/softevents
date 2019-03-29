# Generated by Django 2.1.7 on 2019-03-28 12:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0004_auto_20190328_1254'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookingid', models.CharField(max_length=10)),
                ('date', models.DateTimeField(null=True)),
                ('eventid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='events.Event')),
                ('participantid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moreinfo', models.TextField()),
                ('date', models.DateTimeField(null=True)),
                ('eventid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='events.Event')),
                ('participantid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
