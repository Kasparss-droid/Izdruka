iet=input("Kā tev klājas? ")
print(len(iet))

vards=input("Kā tevi sauc? ")
print(vards[0])

myString="Sveika, pasaule!"
print(myString[10:])

patik=input("Kas tev patīk? ")
print(patik.upper())

nepatik=input("Kas tev nepatīk? ")
print(nepatik.lower())

samercet="samērcēt"
ped_burti=samercet[1:]
print("p"+ped_burti)

pasaule=("  Sveika, Pasaule!  ")
print(pasaule[1:18])

#Uzraksti programmu, kas uzdod 2 jautājumus par telpas izmēriem-platumu un garumu. Aprēķini un izdrukā telpas laukumu.

Platums=int(input("Cik metru liela ir telpas platumā? "))
Garums=int(input("Cik metru liela ir telpas garumā? "))
Laukums=Platums*Garums
print(f"Telpas laukums ir {Laukums} m2.")

vards=input("Kā tevi sauc? ")
x=(vards[::-1])
x=x+(" Pamatīgs juceklis, vai ne, *?")
print(x)