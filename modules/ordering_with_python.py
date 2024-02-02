#!/usr/bin/python3
# coding: utf-8
from operator import itemgetter, attrgetter

divider = "-" * 50
etudiants = [("Clement", 14, 16), ("Charles", 12, 15), ("Oriane", 14, 18), ("Thomas", 11, 19), ("Damien", 12, 15)]

# Le tri sera sur la première colonne [noms]
for elts in sorted(etudiants):
    print(elts)


# Le tri sera sur la troisième colonne [note]
for elts in sorted(etudiants, key=lambda colonne: colonne[2]):
    print(elts)


# avec des class
class Etudiant:

    """Classe représentant un étudiant.

    On représente un étudiant par son prénom (attribut prenom), son âge
    (attribut age) et sa note moyenne (attribut moyenne, entre 0 et 20).

    Paramètres du constructeur :
        prenom -- le prénom de l'étudiant
        age -- l'âge de l'étudiant
        moyenne -- la moyenne de l'étudiant

    """

    def __init__(self, prenom, age, moyenne):
        self.prenom = prenom
        self.age = age
        self.moyenne = moyenne

    def __repr__(self):
        return "<Étudiant {} (âge={}, moyenne={})>".format(self.prenom, self.age, self.moyenne)


# Recréons notre liste :
etudiantsClass = [
    Etudiant("Clément", 14, 16),
    Etudiant("Charles", 12, 15),
    Etudiant("Oriane", 14, 18),
    Etudiant("Thomas", 11, 19),
    Etudiant("Damien", 12, 15),
]

# Le tri en notes
print()
print(divider)
for etudiant in sorted(etudiantsClass, key=lambda etudiant: etudiant.moyenne):
    print(etudiant)

# Le trin en age
print()
for etudiant in sorted(etudiantsClass, key=lambda etudiant: etudiant.age):
    print(etudiant)

# Le trin en age reversed
print()
for etudiant in sorted(etudiantsClass, key=lambda etudiant: etudiant.age, reverse=True):
    print(etudiant)


# tri avec itemgetter de operator:
# Avec une liste de tuple:
for etudiant in sorted(etudiants, key=itemgetter(2)):
    print(etudiant)

# Avec une class selon moyenne:
for etudiant in sorted(etudiantsClass, key=attrgetter("moyenne")):
    print(etudiant)

# selon age est moyenne
for etudiant in sorted(etudiantsClass, key=attrgetter("age", "moyenne")):
    print(etudiant)


class LigneInventaire:

    """Classe représentant une ligne d'un inventaire de vente.

    Attributs attendus par le constructeur :
        produit -- le nom du produit
        prix -- le prix unitaire du produit
        quantite -- la quantité vendue du produit.

    """

    def __init__(self, produit, prix, quantite):
        self.produit = produit
        self.prix = prix
        self.quantite = quantite

    def __repr__(self):
        return "Ligne d'inventaire: {} ({} X {}) = {} ".format(
            self.produit, self.prix, self.quantite, self.prix * self.quantite)


# Création de l'inventaire
inventaire = [
    LigneInventaire("pomme rouge", 1.2, 19),
    LigneInventaire("orange", 1.4, 24),
    LigneInventaire("banane", 0.9, 21),
    LigneInventaire("poire", 1.2, 24),
]

for produit in sorted(inventaire, key=attrgetter("prix", "quantite")):
    print(produit)


inventaire.sort(key=attrgetter("quantite"), reverse=True)
for produit in sorted(inventaire, key=attrgetter("prix")):
    print(produit)
