# funcion para convertir las palabras contenidas en una lista a Mayusculas
def upper_case(lista):
    for i in range(len(lista)):
        lista[i] = lista[i].upper()
    return lista
