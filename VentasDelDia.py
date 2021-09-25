#Una empresa realizo 100 ventas en el dia y desea saber cual fue el importe total de las ventas 
#cuantas de las ventas superaron los $10mil y cuantos fueron inferiores a $1000 

#Declaracion de variables
Ventas=5
Importe= 0
Total= 0
Cont= 0
Cont2= 0
Cont3= 0

#Ingreso de datos
while Cont<Ventas:
	Importe =int(input("Ingrese el valor de su venta : $ "))
	Total= Importe + Total
	Cont +=1
		
	if Importe>10000:
		Cont2 +=1
	elif Importe<1000:
		Cont3 +=1

print("\nEl importe total es de: $" , Total)
print(" La cantidad de ventas  superiores a $10000 es de : " , Cont2 )
print(" La cantidad de ventas inferiores $1000: " , Cont3 )