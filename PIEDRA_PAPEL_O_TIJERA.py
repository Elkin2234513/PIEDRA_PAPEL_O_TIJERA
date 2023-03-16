import random

print("---------------------------")
print("---PIEFRA PAPEL O TIJERA---")
print("---------------------------")

#input
aleatorio = random.randint(0, 3)
elijePC = ""
print("1. piedra")
print("2. papel")
print("3. tijera")
opcion = int(input("Elige tu opcion: "))


#processing

if opcion == 1:
    elijePC = "piedra"
elif opcion == 2:
    elijePC == "papel"
elif opcion == 3: 
    elijePC == "Tijera"
print("Elejiste: ", elijePC)




#output