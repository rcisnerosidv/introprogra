
cond=False
a = 1
b = 0
while cond == False :
	numeros = int(input("Cuantos numeros de la serie Fibonacci necesitas? (Tiene que ser mayor o igual a 5 o menor o igual a 15). "))
	if numeros >= 5 and numeros <= 15:
		cond = True
	else:
		cond = False
		print(str(numeros) + " no esta dentro del rango especificado.")
print("")
print("Serie de Fibonacci: ")
print(str(b) + ", " + str(a), end="")
for i in range (numeros):
	a = a + b
	b = a - b
	print(", "+ str(a), end="")
