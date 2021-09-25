#Declaracion de variables
a= 0
b=0
s=0

#Ingreso del primer nro:
a= int(input("Ingrese el 1er nro: " , ))

#Ingreso del segundo nro:
b = int (input ("Ingrese un 2do nro: " , ))

#Se comparan los nros:
if a>b:
	s= a - b
else:
	s= b - a 

print ("La resta entre el mayor y el menor da como resultado: ", s)
