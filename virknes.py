"""
vards=input("Kā tevi sauc? ")
print(f"Tavs vārds ir {vards}.")

gadi=int(input("Cik tev gadu? "))
print(f"Tev ir {gadi} gadi.")
dzimsGads=2021-gadi
print(f"Tavs dzimšanas gads ir {dzimsGads}.")


#Uzraksti programmu, kas lietotājam lūdz ievadīt temperatūru pēc Celsija un izdrukā šo temperatūru pēc Farenheita skalas.

Temperatūra=int(input("Cik ārā ir grādi Celsijā? "))
print(f"Ārā ir {Temperatūra} grādi Celsija.")
TempF=Temperatūra*9/5+32
print(f"Ārā ir {TempF} grādi Farenheita")

#Uzraksti programmu, kas uzdod 3 jautājumus par telpas izmēriem-platumu, garumu, augstumu. Aprēķini un izdrukā telpas tilpumu.

Platums=int(input("Cik metru liela ir telpas platumā? "))
Garums=int(input("Cik metru liela ir telpas garumā? "))
Augstums=int(input("Cik metru liela ir telpas augstumā? "))
Tilpums=Platums*Garums*Augstums
print(f"Telpas tilpums ir {Tilpums} m2.")
"""

#Strings (rakstzīmju virknes)
print("Sveiki")
print('Sveiki')
print("I'm going on a run")
print('Arī šīs ir "risinājums"')
print("Sveika, \npasaule!") #izdrukā divās rindās
print("Sveika, \tpasaule!") #izdrukā ar tabulācijas atkāpi

#String garums-len()
print(len("Sveiki"))
print(len("Ko tu domā?"))

# [sākums:beigas:solis]
myString="Sveika, pasaule!"
print(myString)
print(myString[0]) #izdrukā pirmo rakstzīmi
print(myString[8]) #izdrukā 9. rakstzīmi
print(myString[13]) #izdrukā 14. rakstzīmi
print(myString[-3]) #izdrukā 14. rakstzīmi
print(myString[-1]) #izdrukā pēdējo rakstzīmi