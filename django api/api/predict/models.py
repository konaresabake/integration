# from django.db import models

# class Commune(models.Model):
#     # Liste des communes françaises principales
#     COMMUNE_CHOICES = [
#         ('Paris', 'Paris'),
#         ('Marseille', 'Marseille'),
#         ('Lyon', 'Lyon'),
#         ('Toulouse', 'Toulouse'),
#         ('Nice', 'Nice'),
#         ('Nantes', 'Nantes'),
#         ('Strasbourg', 'Strasbourg'),
#         ('Montpellier', 'Montpellier'),
#         ('Bordeaux', 'Bordeaux'),
#         ('Lille', 'Lille'),
#         ('Rennes', 'Rennes'),
#         ('Reims', 'Reims'),
#         ('Le Havre', 'Le Havre'),
#         ('Saint-Étienne', 'Saint-Étienne'),
#         ('Toulon', 'Toulon'),
#     ]
    
#     nom = models.CharField(
#         max_length=100,
#         unique=True,
#         choices=COMMUNE_CHOICES
#     )
    
#     def __str__(self):
#         return self.nom

# class Prediction(models.Model):
#     commune = models.ForeignKey(Commune, on_delete=models.CASCADE)
#     annee = models.IntegerField()
#     recettes = models.FloatField()
#     depenses = models.FloatField()
#     date_prediction = models.DateTimeField(auto_now_add=True)
    
#     class Meta:
#         unique_together = ('commune', 'annee')