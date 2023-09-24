def calculator(num1, num2, operator):
    match operator:
        case "add":
            return num1 + num2
        case "subtract":
            return num1 - num2
        case "multiply":
            return num1 * num2
        case "divide":
            return num1 / num2
        
def checkOperacion(op):
    if type(op) is str and (op == "add" or op == "subtract" or op == "multiply" or op == "divide"):
        return True 
    else:
        return False

print("Hello! Welcome to the Python calculator")
print("To exit, write exit")
print("The possible operations are: add, subtract, multiply and divide")

num1 = ""
num1Checked = False
opChecked = False
num2Checked = False
exit = False
while True:
    if not num1:
        while not num1Checked:
            num1 = input("Enter first number: ")
            if num1.lower() == "exit":
                exit = True
                break
            elif not num1.isnumeric():
                print("Remember that you can only enter numerical values")
            else:
                num1Checked = True
                num1 = int(num1)
    
    if exit:
        break
            
    while not opChecked:
        op = input("Enter operation: ")
        if op.lower() == "exit":
            exit = True
            break
        elif not checkOperacion(op):
            print("Remember that you can only write: add, subtract, multiply or divide")
        else:
            opChecked = True
            
    if exit:
        break
            
    while not num2Checked:
        num2 = input("Enter second number: ")
        if num2.lower() == "exit":
            exit = True
            break
        elif not num2.isnumeric():
            print("Remember that you can only enter numerical values")
        else:
            num2Checked = True
            num2 = int(num2)
    
    if exit:
        break

    result = calculator(num1, num2, op)

    print(
        f"The result of {op} {num1} and {num2} is: {result}")

    num1 = result
    opChecked = False
    num2Checked = False
