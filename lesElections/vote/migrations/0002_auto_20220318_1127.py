# Generated by Django 3.2.12 on 2022-03-18 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='idees',
            name='signeAstrologique',
        ),
        migrations.DeleteModel(
            name='SigneAstrologique',
        ),
    ]
