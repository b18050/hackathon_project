# Generated by Django 2.2.2 on 2019-07-08 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mapnav', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_info',
            old_name='amountaz',
            new_name='amount',
        ),
    ]
