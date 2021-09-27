while 1:
    
    nro = int (input("Ingrese un nro entero, le diremos si es primo o no: "))
    divisor = 2

    while nro > divisor:
        if nro%divisor ==0:
            print ("No es primo")
            break
        elif nro%divisor!=0:
            divisor= divisor+1

    if nro==divisor:
        print("Si es primo")