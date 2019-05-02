my_fic = open('test.txt', "a")

print(my_fic)

my_fic.write(" , moi ca va ouais jsuis dans un bon mood")

my_fic.close()

my_fic = open('test.txt', "r")

contenu = my_fic.read()

print(contenu)

my_fic.close()


# toujours refermer le fichier sinon erreur / possibilité de raccourcir le code avec la methode with qui fonctionne comme une boucle. pour entregistrer des objets comme des dicos dans un fichier il faut utiliser pickle

# -*- coding: cp1252 -*-
