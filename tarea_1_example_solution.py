
def operation_selector(num1, num2, op):

    operations = ["+", "-", "*", "&"]

    if isinstance(num1, bool) or isinstance(num2, bool): #Condicional para determinar si las entradas son de tipo Bool y devolver un error
        return -50, None
    if not (isinstance(num1, int) and isinstance(num2, int)): #Condicional para asegurar que se ingresron numeros enteros
        return -50, None
    elif not isinstance(op, str):# Aqui se determina si se ingresó una entrada distinta a un string en la operacion.
        return -60, None
    if isinstance(op, str) and not (op in operations):# Determina si la operación no existe y devuelve el error correspondiente. 
        return -70, None
    elif op == operations[0]: # Operación de suma
        return 0, num1 + num2
    elif op == operations[1]: # Operacion de resta
        return 0, num1 - num2
    elif op == operations[2]: # Operacion de multiplicación
        return 0, num1 * num2
    elif op == operations[3]: # Operación and lógico
        return 0, num1 & num2


def calculo_promedio(lista_valores):
    if len(lista_valores) > 10: # Si la lista de valores es mayor a 10 se devuelve el error correspondiente.
        return -90, None

    if not all(isinstance(item, int) and not isinstance(item, bool) #Aqui se revisa que todos los elementos en la lista sean numeros, sino se devielve el error -80
               for item in lista_valores):
        return -80, None

    return 0, sum(lista_valores)/len(lista_valores) #Se devuevle el promedio de los numeros de la lista.


n, g = calculo_promedio([1, True, 3, 4])
print(g)
 
