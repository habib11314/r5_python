#Entre utilisateur
s=input()
print("Bienvenue "+s)

#Table de multiplication

def table ():
    n=int(input("Entrez un nombre: " ))
    i=0
    while(i < n):
        print(str(i)+"*5="+ str(n*i))
        i+=1

print(table())

#Diviseurs

def diviseurs (b):
    nombre=int(input("Entrez un nombre: " ))
    if nombre <= 0:
        print("Veuillez entrer un nombre positif.")
        return
    while b <= nombre:
        if nombre % b == 0:
            print(b)
        b += 1
print(diviseurs(1))

#Nombres premiers => divisible par lui meme et par 1

def nombre_pre(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
print(nombre_pre(11))

def afficher_nombres_premiers():
    for nombre in range(1, 101):
        if nombre_pre(nombre):
            print(f"{nombre} est premier")

print(afficher_nombres_premiers())

#difference yel et return = yel -> reprends la fonction, return -> sort de la fonction


def hauteurParcourue(n,h)
    for jours in range (1,8):
        
    