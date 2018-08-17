def fibo(num):
    if num == 0:
        return 0
    if num == 1:
        return 1

    return fibo(num-1) + fibo(num-2)

if __name__ == '__main__':
    num = int(input("Cuantos numeros de la serie de Fibonacci quieres?"))
    for i in range(num):
        print(str(fibo(i)) + ", ", end="")
    print("")