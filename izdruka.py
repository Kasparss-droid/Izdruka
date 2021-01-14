"""Var rakstīt komentārus
vairākās
rindās"""
print("Sveika, pasaule!")
print(2*2)
print(2*2, 2*3, 2*4, "Pitons")
print(f"Ja saskaitīsim 5 ar 7, iegūsim {5+7}.") #kombinētā izdruka - teksts un aprēķins
print("Sveika, "+"pasaule!")
print("Roberts "*5)
print(f"Šogad ir {60*60*24*365} sekundes.")
print(0.1 + 0.2 - 0.3)
print()

#Mainīgie
a=5
print(a)
print(a+a)
a=a+a #Zīme=nozīmē piešķiršanu
print(a)
print(type(a))
a=30.1
print(type(a))

mani_ienakumi=430
nodoklis=0.23 #10%
maniNodokli=mani_ienakumi*nodoklis
print(maniNodokli)

#help
help("keywords")

#Datu ievade-input
print("Ievadi vārdu: ")
x=input()
print("tavs ievadītais vārds ir "+x)

#Otrā versija
x=input("Ievadi vārdu: ")
print("tavs ievadītais vārds ir "+x)

#Skaitļu ievade
sk=int(input("Ievadi veselu skaitli: ")) #pārveido ievadīto datu tipu pat int
print(f"Tavs ievadītais skaitlis ir {sk}.")