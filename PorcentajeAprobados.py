#Hacer un programa, que permita, ingresar los promedios de una asignatura en un curso y 
#que calcule cuantos alumnos estan aprobados y cuantos desaprobados, indicando tambien el procentaje en ambos casos.

promedio=0
aprobados=0
desaprobados=0
cont=0
porcaprov=0
porcdesa=0
alumnos=0

alumnos=int(input("Ingresar la cantidad de alumnos en un curso: "))
	
while cont<alumnos:
	promedio=float(input("Ingresar el promedio de la asignatura: "))
	cont+=1

	if promedio>5:
		aprobados+=1

	elif promedio<6:
		desaprobados+=1


porcaprov= (aprobados*100)/alumnos
porcdesa= (desaprobados*100)/alumnos

print("\nEstos son los resultados:"6)
print(" La cantidad de alumnos aprobados son: ",aprobados)
print (" Siendo un porcentaje de: %", porcaprov)
print("\n La cantidad de alumnos desaprobados son: ",desaprobados )
print(" Siendo un porcentaje de: %", porcdesa)
