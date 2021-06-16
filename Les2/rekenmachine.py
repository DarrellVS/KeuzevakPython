memory = {}


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

def store():
    name = input("Provide a key on which to store the value: ")
    value = int(input("Enter a value to store: "))
    memory[name] = value
    print(f"Stored the value {value} to key {name}")
    


while True:
    # Take input from the user  
    select = input("Please select operation -\n Add\n Subtract\n Multiply\n Divide\n Store\n") 
    
    if select == "Add": 
        inpt = getInput()
        print(inpt[0] + inpt[1]) 

    elif select == "Subtract": 
        inpt = getInput()
        print(inpt[0] - inpt[1]) 
    
    elif select == "Multiply": 
        input = getInput()
        print(inpt[0] * inpt[1]) 
    
    elif select == "Divide": 
        input = getInput()
        print(inpt[0] / inpt[1]) 

    elif select == "Store":
        store()

    else: 
        print("Invalid input") 

    print("\n\n\n\n")