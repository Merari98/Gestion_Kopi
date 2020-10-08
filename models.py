# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Comptabilite(models.Model):
    point_boutique = models.IntegerField()
    point_livraison = models.IntegerField()
    argent_om = models.IntegerField()
    depense = models.IntegerField()
    motif_depense = models.TextField()
    en_caisse = models.IntegerField()
    prevision_caisse = models.IntegerField()
    date = models.DateTimeField()
    updated_at = models.DateTimeField()
    loggerid = models.IntegerField()
    id_pays = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'comptabilite'


class Livraison(models.Model):
    id = models.AutoField(unique=True)
    contact = models.CharField(max_length=255)
    nom_produit = models.CharField(max_length=255)
    type_produit = models.CharField(max_length=255)
    quantité = models.IntegerField()
    commune = models.CharField(max_length=255)
    expedition = models.IntegerField()
    date = models.DateTimeField()
    updated_at = models.DateTimeField()
    loggerid = models.IntegerField()
    id_pays = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'livraison'


class Om(models.Model):
    montant = models.IntegerField()
    date = models.DateField()
    observation = models.TextField()
    loggerid = models.IntegerField()
    id_pays = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'om'


class Pays(models.Model):
    nom_pays = models.CharField(max_length=255)
    commentaire = models.TextField()

    class Meta:
        managed = False
        db_table = 'pays'


class Produit(models.Model):
    nom = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    loggerid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'produit'


class Satus(models.Model):
    nom = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'satus'


class Stock(models.Model):
    id_produit = models.IntegerField()
    stock_livreur = models.IntegerField()
    stock_agence = models.IntegerField()
    nombre_sachets = models.IntegerField()
    nombre_boites = models.IntegerField()
    date = models.DateTimeField()
    updated_at = models.DateTimeField()
    loggerid = models.IntegerField()
    id_pays = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stock'


class User(models.Model):
    nom = models.CharField(max_length=255)
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    role = models.IntegerField()
    id_pays = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user'
