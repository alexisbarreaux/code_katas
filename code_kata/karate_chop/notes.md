# Notes

## First method

Erreur car il faut gérer le fait qu'ici c'est pas juste une recherche dichotomique avec un booléen, mais qu'on veut la position,
ce qui inclut le fait de décaler les valeurs renvoyées.

Version récurrente assez naturelle et concise.

## Second method

boucle infinie (a-b//2 au lieu de a+b//2)
Rapide

## Third method

Chiant, pas mal d'erreurs.

## Fourth method

forgot offset and end condition on one element list
pire des 4
détruit la liste, donc bof

## Fifth method

encore plus affreux avec un pointeur à gérer, boucle infinie à gérer.
Offset inutile utilisé au début.
Très désagréable et franchement pas très beau.