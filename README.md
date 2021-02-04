Ecrire les actions paramétrées (procedure ou fonction) permettant de resoudre les problèmes suivants :
Calcul de la somme de deux nombres entiers.
Calcul de la factorielle de N (N !).
Vérifier si un nombre entier A divise un nombre entier B.
Calcul du quotient et du reste de la division entière de deux nombres entiers A et B.
Vérifier si un caractère donné est une voyelle (voyelles : 'a', 'e', 'i', 'o', 'u', 'y').
Permet de permuter (d'échanger) le contenu de deux variables réelles.
Étant donné un entier A, calculé sa valeur absolue.


Fonction Somme(x,y :entier) :entier ;
Debut
Somme — x+y ;
Fin ;

Fonction Fact(x:entier) :entier ;
Var I,F :entier ;
Debut
F—1 ; /* on peut utiliser directement le nom de la fonction au lieu de F
Pour I—1 a x Faire F — F*I ; Fait ;
Fact — F ;
Fin ;


Fonction Divise(A,B :entier) :booleen ;
Debut
Divise — Faux ;
Si B mod A = 0 Alors Divise — Vrai Fsi ;
Fin ;

Procedure QuotRest(E/ A,B :entier ; S/ Q,R :entier) ;
Debut
Q — 0 ; R — A ;
Tantque R>= B Faire
R — R mod B ;
Q - Q+1 ;
Fait ;
Fin ;

Fonction Voyelle(C :caractere) :booleen ;
Debut
Voyelle — Faux ;
Cas C Vaut
'a', 'e', 'i', 'o', 'u', 'y': Voyelle — Vrai ;
Fincas ;
Fin ;

Procedure Permute(E/S/ A,B :entier ) ;
Var C:entire:
Debut
C — A ; A — B ; B — C ;
Fin ;


Fonction Vabs(A :entier) :entier ;
Debut
Vabs — A ;
Si A<0 Alors Vabs — A Fsi;
Fin ;
