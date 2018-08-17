def factorial(num):
    if(num == 1):
        return 1
    else:
        return num * factorial(num-1)
      

if __name__ == '__main__':
    num = int(input("Ingresa el numero para saber su factorial: "))
    print(factorial(num))
