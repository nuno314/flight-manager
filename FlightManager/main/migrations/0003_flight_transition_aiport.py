# Generated by Django 4.0.3 on 2022-05-10 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_airport_flight_policy_ticketclass_transitionairport_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='transition_aiport',
            field=models.ManyToManyField(to='main.transitionairport'),
        ),
    ]