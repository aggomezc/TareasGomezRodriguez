def operation_selector(num1, num2, op):
    operations = ["+", "-", "*", "&"]
    
    if isinstance(num1, bool) or isinstance(num2, bool):
        return -50, None
    if not(isinstance(num1,int) and isinstance(num2,int)):
        return -50, None
    elif not isinstance(op, str):
        return -60, None
    if isinstance(op, str) and not(op in operations):
        return -70, None
    elif op == operations[0]:
        return 0, num1 + num2
    elif op == operations[1]:
        return 0 , num1 - num2
    elif op == operations[2]:
        return 0, num1 * num2
    elif op == operations[3]:
        return 0, num1 & num2



def calculo_promedio(lista_valores):
    if len(lista_valores)>10:
        return -90, None

    if not all(isinstance(item, int) and not isinstance(item, bool) for item in lista_valores):
        return -80, None
    
    return 0, sum(lista_valores)/len(lista_valores)
n,g = calculo_promedio([1, True, 3, 4])
print(g)

