# Notes

## First method

Erreur car il faut gérer le fait qu'ici c'est pas juste une recherche dichotomique avec un booléen, mais qu'on veut la position,
ce qui inclut le fait de décaler les valeurs renvoyées.

Version récurrente assez naturelle et concise.

## Second method

boucle infinie (a-b//2 au lieu de a+b//2)
Rapide

## Third method

Moins évident, pas mal d'erreurs.

## Fourth method

pire des 4
détruit la liste, donc peut pertinent dans la plupart des cas à mon avis.

## Fifth method

encore plus affreux avec un pointeur à gérer, boucle infinie à gérer.
Offset inutile utilisé au début.
Très désagréable et franchement pas très beau.