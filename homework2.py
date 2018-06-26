import os

def directories(path):
    dir = os.listdir(path)
    for i in dir:
        print(i)

def txtfile():
    file = open('hola.txt', 'w')
    file.write('Hola, mi nombre es Rodolfo: \nTe saludo desde mi primer archivo de texto. \n \n \n Saludos!')
    file.close
    print("Archivo .txt creado con exito, echale un vistaso ;) ")

def abs(file):
    absol = os.path.abspath(file)
    return absol

def matches():
    file3 = open('match.txt', 'w')
    with open('primos.txt', 'r') as file1:
        with open('felices.txt', 'r') as file2:
            list1 = file1.readlines()
            list2 = file2.readlines()
            for i in range (len(list1)):
                for j in range (len(list2)):
                    if(int(list1[i]) == int(list2[j])):
                        file3.write(list1[i])
        file1.close
        file2.close
        file3.close

    
def main():
    option = int(input("Introduce la opcion deseada: "))
    if(option == 1):
        direct = input("Introduce la ruta para ver los directorios que contiene: ")
        directories(direct)
    elif(option == 2):
        txtfile()
    elif(option == 3):
        arc = input("Introduce la ruta y nombre de tu archivo para saber la ruta absoluta: ")
        absol = abs(arc)
        print("La ruta absoluta de tu archivo es: " + absol)
    elif(option == 4):
        matches()
    else:
        print("Opcion no valida")

if __name__ == '__main__':
    main()
