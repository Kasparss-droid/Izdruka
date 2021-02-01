#string metodes
vards="Man" #Ko darīt, lai nomainītu uz Gan?
ped_burti=vards[1:]
print("G"+ped_burti) #string konkatinācija

#string konkatinācija
x="Sveika, pasule, "
x=x+"kā klājas?"
print(x)

print(5+6)
print("5"+"6")
#nedrīkst saskaitīt string ar skaitļiem

print(x.upper()) #uzraksta ar lielajiem burtiem
print(x.lower()) #uzraksta ar mazajiem burtiem
x2=x.upper()
print(x2)

print(x.split()) #sadala visu pa daļām, izmantojot atstarpi
print(x.split("a")) #sadala visu pa daļām, izmantojot "a"