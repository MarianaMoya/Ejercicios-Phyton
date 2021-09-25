#Una empresa realizo en un mes 730 facturas y desea saber cuantas hizo a consumidor final, a monotributistas, a responsables inscriptos y a otros

facturas = ""
consufinal = 0 
monotributistas = 0
resinsciptos = 0
otros = 0
cont = 0


while cont<5:
	facturas = str(input("Ingresar tipo de factura:\n -Consumidor final -> presione A \n -Monotributista -> presione B\n -Resp. Inscripto -> presione C \n -Otro -> presione D \n " ))
	cont = cont+1

	if facturas == "A" or facturas == "a":
		consufinal+= 1

	elif facturas == "B" or facturas == "b":
		monotributistas+= 1

	elif facturas == "C" or facturas ==  "c":
		resinsciptos+= 1

	elif facturas == "D" or facturas == "d":
		otros+= 1 	

print("Facturas a consumidor final:"  ,consufinal)
print("Facturas a monotributistas:"  ,monotributistas)
print("Facturas a responsables inscriptos:"  ,resinsciptos)
print("Facturas a otros:"  ,otros)