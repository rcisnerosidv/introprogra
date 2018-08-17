class alumno:
    def __init__(self, Nombre, Promedio, Grupo):
        self.Nombre = ""
        self.Promedio = 0.0
        self.Grupo = ""

def grupos():

    g16A = open('2016A.txt', 'w')
    g16B = open('2016B.txt', 'w')
    g17A = open('2017A.txt', 'w')
    g17B = open('2017B.txt', 'w')
    g18A = open('2018A.txt', 'w')
    g18B = open('2018B.txt', 'w')

    g2016A = []
    g2016B = []
    g2017A = []
    g2017B = []
    g2018A = []
    g2018B = []

    with open('Estudiantes.txt','r') as file1:
        lista1 = file1.readlines()
    for i in range(len(lista1)):
        lista2 = lista1[i].split(',')

        if lista2[2] == ' 2016A\n' :
           g2016A.append(lista1[i])

        elif lista2[2] == ' 2016B\n':
           g2016B.append(lista1[i])

        elif lista2[2] == ' 2017A\n':
           g2017A.append(lista1[i])

        elif lista2[2] == ' 2017B\n':
           g2017B.append(lista1[i])

        elif lista2[2] == ' 2018A\n':
           g2018A.append(lista1[i])

        elif lista2[2] == ' 2018B\n':
           g2018B.append(lista1[i])

    for i in range(len(g2016A)):
        g16A.write(str(g2016A[i]))
   
    for i in range(len(g2016B)):
        g16B.write(str(g2016B[i]))
 
    for i in range(len(g2017A)):
        g17A.write(str(g2017A[i]))
  
    for i in range(len(g2017B)):
        g17B.write(str(g2017B[i]))
   
    for i in range(len(g2018A)):
        g18A.write(str(g2018A[i]))
  
    for i in range(len(g2018B)):
        g18B.write(str(g2018B[i]))
 
def agregar(listAlumno):
    name = input("Ingrese el nombre del alumno: ")
    av = str(input("Ingrese el promedio del alumno: "))
    group = str(input("Ingrese el grupo del alumno: "))
    nuevo = alumno(name, av, group)
    nuevoestudiante = open('Estudiantes.txt','a')
    nuevoestudiante.write(name + ', ' + av + ', ' + group + '\n') 
    listAlumno.append(nuevo)
    nuevoestudiante.close

    return listAlumno

def objetoAlumno():
    ListaAlumnos = []
    with open('Estudiantes.txt', 'r') as file1:
        lista3 = file1.readlines()
    for i in range (len(lista3)):
        a = lista3[i].split(', ')
        objalum = alumno(a[0], a[1], a[2])
        ListaAlumnos.append(objalum)

    return ListaAlumnos

def alphaSort(alum, num):
    if num == 0:
        return alum
    alpha = alphasort(alum, num-1)
    for i in range(1, (len(alpha) + 1 - num)):
        if alpha[i-1].Nombre > alpha[i].Nombre:
            mayor = alfabetico[i]
            alpha[i] = alpha[i-1]
            alpha[i-1] = mayor

    return alpha

def avSort(alum, num):
    if num == 0:
        return alum
    average = avSort(alum, num-1)
    for i in range(1, (len(average) + 1 - num)):
        if average[i-1].Promedio < average[i].Promedio:
            mayor = average[i]
            average[i] = average[i-1]
            average[i-1] = mayor

    return average


def main():
    x = objetoAlumno()
    print("1. Separar Nombres por grupo en archivos diferentes, 2. Agregar Alumno, 3. Ordenar Alfabeticamente, 4. Ordenar por promedio  ")
    case = input("Que deseas hacer? ")
    if (case == 1):
        grupos()
        print("Operación realizada con éxito ")
    elif (case == 2):
        agregar(x)
    
    elif (case == 3):
        myList = ordenProm(x, len(x))
        Alfabetico = open('Alfabetico.txt','w')
        for i in range(len(myList)):
            Alfabetico.write(str(myList[i].nombre)+', '+str(myList[i].promedio)+', '+str(myList[i].grupo))

    elif (case == 4):
       myList = ordenProm(x, len(x))
       Promedio = open('Promedio.txt','w')
       for i in range(len(myList)):
            Promedio.write(str(myList[i].nombre)+', '+str(myList[i].promedio)+', '+str(myList[i].grupo))






if __name__ == "__main__":
    main()