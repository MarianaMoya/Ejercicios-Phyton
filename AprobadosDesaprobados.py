#22 alumnos ingresan el promedio de cada uno de ellos.Contar cuantos estan aprobados,desaprobados y cuantos tienen aplazo dentro de los desaprobados.
#Declaracion de variables
Nota=0
Aprob=0
Desaprob=0
Aplaz=0
CantAlum=0

#Ingresan las calificaciones
while CantAlum<10:
	Nota = int(input("Ingrese su calificación:  "  ))
	CantAlum +=1
	
	if Nota>=6:
		Aprob +=1
	else: 
		Desaprob +=1
	if Nota<4:
		Aplaz +=1

print("\nLa cantidad de aprobados es de :  " , Aprob)
print("La cantidadde desaprobados es de: " , Desaprob)
print("La cantidad de aplazados es de: " , Aplaz)
		