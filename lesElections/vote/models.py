from django.db import models

# Create your models here.
class Penseur(models.Model):
    pseudoPenseur = models.CharField(max_length=60)

    def __str__(self):
        return self.pseudoPenseur

class Idees(models.Model):
    nomIdee = models.CharField(max_length=60)
    typeIdee = models.CharField(max_length=60)
    dateIdee = models.DateTimeField('Date de création de l\'idée')
    penseur = models.ForeignKey(Penseur, on_delete=models.CASCADE)

    def __str__(self):
        return self.nomIdee

class Chevelure(models.Model):
    typeChevelure = models.CharField(max_length=60)
    tailleChevelure = models.IntegerField(default=0)

    def __str__(self):
        return self.typeChevelure

class Roles(models.Model):
    nomRole = models.CharField(max_length=60)
    nbVoteRole = models.IntegerField(default=1)

    def __str__(self):
        return self.nomRole

class Votants(models.Model):
    nomVotant = models.CharField(max_length=60)
    prenomVotant = models.CharField(max_length=60)
    mailVotant = models.CharField(max_length=100)
    voteVotant = models.BooleanField(default=False)
    chevelure = models.ForeignKey(Chevelure, on_delete=models.CASCADE)
    roles = models.ForeignKey(Roles, on_delete=models.CASCADE)

    def __str__(self):
        return self.nomVotant, self.prenomVotant

class Voter(models.Model):
    nbVote = models.IntegerField(default=0)
    idees = models.ForeignKey(Idees, on_delete=models.CASCADE)
    votants = models.ForeignKey(Votants, on_delete=models.CASCADE)

    def __str__(self):
        return self.nbVote