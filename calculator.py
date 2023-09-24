def calculator(num1, num2, operator):
    match operator:
        case "sumar":
            return num1 + num2
        case "restar":
            return num1 - num2
        case "multiplicar":
            return num1 * num2
        case "dividir":
            return num1 / num2
        
def checkOperacion(op):
    if type(op) is str and (op == "sumar" or op == "restar" or op == "multiplicar" or op == "dividir"):
        return True 
    else:
        return False

print("Hola, bienvenido/a a la calculadora de Python")
print("Para salir, escribe salir")
print("Las operaciones posibles son: sumar, restar, multiplicar y dividir")

num1 = ""
num1Checked = False
opChecked = False
num2Checked = False
while True:
    if not num1:
        while not num1Checked:
            num1 = input("Ingrese primer número: ")
            if num1.lower() == "salir":
                break
            elif not num1.isnumeric():
                print("Recuerde que solo puede introducir valores numéricos")
            else:
                num1Checked = True
                num1 = int(num1)
            
    while not opChecked:
        op = input("Ingrese operación: ")
        if op.lower() == "salir":
            break
        elif not checkOperacion(op):
            print("Recuerde que solo puede introducir - sumar, restar, multiplicar o dividir")
        else:
            opChecked = True
            
    while not num2Checked:
        num2 = input("Ingrese segundo número: ")
        if num2.lower() == "salir":
            break
        elif not num2.isnumeric():
            print("Recuerde que solo puede introducir valores numéricos")
        else:
            num2Checked = True
            num2 = int(num2)

    resultado = calculator(num1, num2, op)

    print(
        f"El resultado de {op} {num1} y {num2} es: {resultado}")

    num1 = resultado
    opChecked = False
    num2Checked = False
