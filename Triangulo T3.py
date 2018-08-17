def Triangulo(n): 

    if n == 0: 

        return [] 

    if n == 1: 

        return [[1]] 

    lista1 = Triangulo(n-1) 
    lista2 = [1] 

    for i in range(1, n-1): 
        lista2.append(lista1[n-2][i-1] + lista1[n-2][i]) 

    lista2.append(1) 
    lista1.append(lista2) 

    return lista1

     

def linea(n):
    triangle = Triangulo(n) 

    return triangle[n-1] 

def main():
   n = int(input("Cuatas lineas quieres para el triangulo de pascal? "))
   res= Triangulo(n)

   for i in res:
        print(i)

if __name__ == "__main__":
    main()