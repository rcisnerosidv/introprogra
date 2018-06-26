def Saludar():
	print("Hola bienvenido a mi primer programa hecho con funciones")

def Suma(numX, numY):
	if(type(numX) != int or type(numY) != int):
		print("Estas usando un tipo de dato incorrecto.")
		return
	result = numX + numY
	return result

def Resta(numX, numY):
	if(type(numX) != int or type(numY) != int):
		print("Estas usando un tipo de dato incorrecto.")
		return
	result = numX - numY
	return result

def Multi(numX, numY):
	if(type(numX) != int or type(numY) != int):
		print("Estas usando un tipo de dato incorrecto.")
		return
	result = numX*numY
	return result

def Div(numX, numY):
	if(type(numX) != int or type(numY) != int):
		print("Estas usando un tipo de dato incorrecto.")
		return
	result = numX / numY
	return result

def Pot(numX, numY):
	if(type(numX) != int or type(numY) != int):
		print("Estas usando un tipo de dato incorrecto.")
		return
	for i in range(numY):
		result = numX*numX
	return result
#Funcion principal del programa
def main():
	Saludar()
	print("Que operacion quieres realizar?")
	opcion = int(input("1. Suma, 2. Resta, 3. Multiplicacion, 4. Division, 5. Potencia "))
	if(opcion >= 1 and opcion <= 5):
		if(opcion == 1):
			num1 = int(input("Escribe un numero: "))
			num2 = int(input("Escribe otro numero: "))
			result = Suma(num1, num2)
			print("El resultado de la suma es: " + str(result))
			
		if(opcion == 2):
			num1 = int(input("Escribe un numero: "))
			num2 = int(input("Escribe otro numero: "))
			result = Resta(num1, num2)
			print("El resultado de la resta es: " + str(result))
			
		if(opcion == 3):
			num1 = int(input("Escribe un numero: "))
			num2 = int(input("Escribe otro numero: "))
			result = Multi(num1, num2)
			print("El resultado de la multiplicacion es: " + str(result))
			
		if(opcion == 4):
			num1 = int(input("Escribe un numero: "))
			num2 = int(input("Escribe otro numero: "))
			if(num2 == 0):
				print("No puedes dividir entre cero")
				return
			result = Div(num1, num2)
			print("El resultado de la division es: " + str(result))
			
		if(opcion == 5):
			num1 = int(input("Escribe un numero: "))
			num2 = int(input("A que potencia lo quieres elevar?: "))
			result = Pot(num1, num2)
			print("El resultado de la potencia es: " + str(result))

		#else:
			#print ("Opcion no valida")
if __name__ == "__main__":
	main()	