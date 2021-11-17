texto = """El texto argumentativo tiene como principal objetivo dar sustento a la tesis formulada por 
el autor mediante la exposición coherente y lógica de justificaciones o razones, que tienen 
como propósito persuadir o convencer al lector sobre un punto de vista predeterminado.
La argumentación hace referencia a la exposición de un conjunto de razones con el propósito 
de demostrar o justificar una cosa. En consecuencia, la argumentación no suele darse en estado 
puro y suele combinarse con la exposición. Mientras la exposición se limita a mostrar, 
la argumentación intenta demostrar, persuadir, convencer o cambiar ideas. Por ello, en un 
texto argumentativo, además de la función apelativa presente en el desarrollo de las 
declaraciones, lo que nos enseña aparece la función representativa, en la parte en la que 
se expone la tesis."""

# Voy a  definir los caracteres que no hay que contar
fuera = ",;.:\n!\"'"

# Reemplazo "fuera" por NADA, o sea remover        
for caracter in fuera:
        texto = texto.replace(caracter, "") 

# Convertimos a minuscula todas las palabras
texto = texto.lower()

# Todas las cadenas estan separadas por un espacio, lo usamos como separador,
# asi que convertimos la cadena a arreglo
palabras = texto.split(" ")

# Vamos a crear un diccionario para contar las palaras. 
# En este caso la clave del diccionario sera la palabra, y el valor sera el conteo
diccionario_frecuencias = {}
for palabra in palabras:
    if palabra in diccionario_frecuencias:
        diccionario_frecuencias[palabra] +=1 #diccionarioDeFrec en la posicion palabra incrementa en 1 (palabra existente)
    else:
        diccionario_frecuencias[palabra] = 1 #idem, palabra nueva

for palabra in diccionario_frecuencias:
    frecuencia = diccionario_frecuencias[palabra]
    print(f"La palabra '{palabra}' tiene ua frecuencia de {frecuencia}")

    

