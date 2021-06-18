import math

memory = {}

validCommands = ["Add", "Subtract", "Multiply", "Divide", "Sin", "Arcsin", "Cos", "Arccos", "Tan", "Arctan", "Sqrt", "Exp", "Ln"]


def getValueForInput(input):
    if(isinstance(input, str)):
        if(input in memory):
            return memory[input]

    return int(input)

def getInput():
    num1 = getValueForInput(
        input("Enter first number: ")
    )
    num2 = getValueForInput(
        input("Enter second number: ")
    )
    return (num1,num2)

def getSingleInput():
    return getValueForInput(input("Enter a number: "))

def store():
    name = input("Provide a key on which to store the value: ")
    value = int(input("Enter a value to store: "))
    memory[name] = value
    print(f"Stored the value {value} to key {name}")
    


while True:
    # Take input from the user  
    commandStr = "\n - ".join(validCommands)
    select = input(f"Please select an operation: \n - {commandStr}\n")
    
    if select == "Add": 
        inpt = getInput()
        print(inpt[0] + inpt[1]) 

    elif select == "Subtract": 
        inpt = getInput()
        print(inpt[0] - inpt[1]) 
    
    elif select == "Multiply": 
        inpt = getInput()
        print(inpt[0] * inpt[1]) 
    
    elif select == "Divide": 
        inpt = getInput()
        print(inpt[0] / inpt[1])

    elif select == "Sin": 
        print(math.sin(getSingleInput()))
        
    elif select == "Arcsin": 
        print(math.asin(getSingleInput()))

    elif select == "Cos": 
        print(math.cos(getSingleInput()))

    elif select == "Arccos": 
        print(math.acos(getSingleInput()))

    elif select == "Tan": 
        print(math.tan(getSingleInput()))

    elif select == "Arctan": 
        print(math.atan(getSingleInput()))

    elif select == "Sqrt": 
        print(math.sqrt(getSingleInput()))

    elif select == "Exp": 
        print(math.exp(getSingleInput()))

    elif select == "Ln": 
        print(math.log(getSingleInput()))

    elif select == "Store":
        store()

    else: 
        print("Invalid input") 

    print("\n\n\n\n")