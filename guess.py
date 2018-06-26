from random import randint

x = randint(0, 9)
kill = False

while(kill == False):
    num = int(input("Trata de adivinar el numero entre 0 y 9 "))
    if(num == x):
        print("Felicidades Adivinaste el número! ")
        kill = True
    elif(num <= x):
        print("El numero que ingresaste es menor, sigue intentando ")
        print("Ingresaste: " + str(num))
        kill = False
    elif(num >= x):
        print("El numero que ingresaste es mayor, sigue intentando ")
        print("Ingresaste: " + str(num))
        kill = False