#En una hay 200 alumnos de 1° y 2° año. La escuela desea saber cuantos alumnos tiene de 12, 13, 14 y mas de 14 años.

#Declaracin de variables.
edad= 0
ContDoce= 0
ContTrece=0
ContCatorce=0
ContMCatorce=0
Cont=0

#Ingreso de datos.

while Cont<10:
	edad= int(input("Ingrese su edad, presione Enter y deje pasar al siguiente: "))

	while True:
		if edad<12:
			print("La edad ingresada debe ser mayor a 11. ")
			edad= int(input("Ingrese su edad nuevamente: "))
		else:
			break

	Cont+=1

	if edad==12:
		ContDoce+=1
	elif edad==13:
			ContTrece+=1
	elif edad==14:
			ContCatorce+=1
	elif edad>14:
			ContMCatorce+=1

print ("\nA continuación se mostraran los datos ingresados " )
print (" La cantidad de alumnos de 12 años es de: " , ContDoce)
print (" La cantidad de alumnos de 13 años es de : " ,ContTrece)
print (" La cantidad de alumnos de 14 años es de : " ,ContCatorce)
print (" La cantidad de alumnos mayores de 14 años es de : " , ContMCatorce)