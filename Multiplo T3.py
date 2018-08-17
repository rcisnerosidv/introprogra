def multiplo(num):
    if num == 0:
        return 0
    else:
        return num + multiplo(num - 3)

if __name__ == '__main__':
    num = int(input("Ingresa un numero "))
    print(multiplo(num))
    
