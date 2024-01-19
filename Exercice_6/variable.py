"""prenom = "Pierre"
nom = "Dupont"
Le but de cet exercice est d'assigner à la variable resultat la chaîne de caractères 'Bonjour je 
m'appelle Pierre Dupont', en utilisant les variables nom et prenom."""
prenom = "pierre"
nom = "Dupont"
phrase = "Bonjour je m'appelle"
resultat = "Bonjour je m'appelle {} {}".format(nom,prenom)
print(resultat)