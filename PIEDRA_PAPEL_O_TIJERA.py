import random

print("---------------------------")
print("---------------------------")
print("---------------------------")
print("---PIEDRA PAPEL O TIJERA---")
print("---------------------------")
print("---------------------------")
print("---------------------------")
print("---------------------------")
print("-------PIEDRA = 1----------")
print("-------PAPEL =  2----------")
print("-------TIJERA = 3----------")
print("---------------------------")
print("---------------------------")


usuario = int(input("DIGITE UN NUMERO: "))
PC = random.randint(1,3)



if usuario == 1 and PC == 2:
    print("GANASTE") 
else:
    if usuario == PC:
        print("EMPATE")
    else:
        if usuario == 2 and PC == 3:
            print("PERDISTE")
        else: 
            if usuario == 3 and PC == 1:
                print("PERDISTE")  
            else:
                if usuario == 2 and PC == 1:
                    print("GANASTE")
                else:
                    if usuario == 3 and PC == 2:
                        print("GANASTE")
                    else:
                        print("PERDISTE")







