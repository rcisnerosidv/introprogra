def suma(numX,numY):
	if(operacion== "-"):
		res = numX + (numY * -1)
	elif (operacion == "+"):
		res = numX + numY
	return res

def multi(numX,numY):
	res = numX * numY
	return res

def div(numX, numY):
	if(numY == 0):
		print("No se puede dividir entre 0")
	else:
		res = numX / numY
	return res

def pot(numX, numY):
	if(numY == 0):
		res = 1
	else:
		for i in range(numY):
			res = numX*numY
	return res

def main():
	op = input("Escribe la operacion que quieras realizar (limitado a 2 numeros separados por espacio)")
	myList = op.split(" ")
	if(myList[1] == "+" or myList[1] == "-"):
		num1 = int(myList[0])
		num2 = int(myList[2])
		operacion = str(myList[1])
		res = suma(num1, num2)
		print(res)
	if(myList[1] == "*"):
		num1 = int(myList[0])
		num2 = int(myList[2])
		operacion = str(myList[1])
		res = multi(num1, num2)
	if(myList[1] == "/"):
		num1 = int(myList[0])
		num2 = int(myList[2])
		operacion = str(myList[1])
		res = div(num1, num2)
	if(myList[1] == "^"):
		num1 = int(myList[0])
		num2 = int(myList[2])
		operacion = str(myList[1])
		res = pot(num1, num2)

if __name__ == '__main__':
	main()
