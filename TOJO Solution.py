"""
	Solution du test en python
	ANDRIANARIJAONA TOJONIRINA

"""
# Calcul de la somme de deux nombres entiers.
def Somme(x,y):
	somme = x + y
	return somme

# Calcul de la factorielle de N (N !).
def Fact(x):
	F=1
	for I in range(1,x+1):
		F = F * I
	Fact = F
	return Fact	

# Vérifier si un nombre entier A divise un nombre entier B.

def Divise(A,B):
	Divise = False
	if A % B == 0:
		Divise = True

	return Divise	

# Calcul du quotient et du reste de la division entière de deux nombres entiers A et B.

def QuotRest(A,B):
	Q = 0
	R = A
	while R>= B:
		R = R % B
		Q = Q + 1
	return Q , R 	


# Vérifier si un caractère donné est une voyelle (voyelles : 'a', 'e', 'i', 'o', 'u', 'y').

def Voyelle(C):
	Voyelle = False
	if C=='a' or C=='e' or C=='o'or C=='u'or C=='i'or C=='y':
		Voyelle = True
	return Voyelle

# Permet de permuter (d'échanger) le contenu de deux variables réelles.

def Permute(A,B):
	C = A
	A = B
	B = C
	return A , B



# Étant donné un entier A, calculé sa valeur absolue.

def Vabs(A):
	Vabs = A
	if A<0:
		Vabs = -A
	return Vabs	

