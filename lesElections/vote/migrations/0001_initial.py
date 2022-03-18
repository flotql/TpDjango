# Generated by Django 3.2.12 on 2022-03-18 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chevelure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeChevelure', models.CharField(max_length=60)),
                ('tailleChevelure', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Idees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomIdee', models.CharField(max_length=60)),
                ('typeIdee', models.CharField(max_length=60)),
                ('dateIdee', models.DateTimeField(verbose_name="Date de création de l'idée")),
            ],
        ),
        migrations.CreateModel(
            name='Penseur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pseudoPenseur', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomRole', models.CharField(max_length=60)),
                ('nbVoteRole', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='SigneAstrologique',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomSigneAstrologique', models.CharField(max_length=60)),
                ('elementSigneAstrologique', models.CharField(max_length=60)),
                ('moisSigneAstrologique', models.DateTimeField(verbose_name='Date du signe astrologique')),
            ],
        ),
        migrations.CreateModel(
            name='Votants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomVotant', models.CharField(max_length=60)),
                ('prenomVotant', models.CharField(max_length=60)),
                ('mailVotant', models.CharField(max_length=100)),
                ('voteVotant', models.BooleanField(default=False)),
                ('chevelure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vote.chevelure')),
                ('roles', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vote.roles')),
            ],
        ),
        migrations.CreateModel(
            name='Voter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nbVote', models.IntegerField(default=0)),
                ('idees', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vote.idees')),
                ('votants', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vote.votants')),
            ],
        ),
        migrations.AddField(
            model_name='idees',
            name='penseur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vote.penseur'),
        ),
        migrations.AddField(
            model_name='idees',
            name='signeAstrologique',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vote.signeastrologique'),
        ),
    ]
