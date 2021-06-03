Add = "Add"
Subtract = "Subtract"
Multiply = "Multiply"
Divide = "Divide"

while True:
    # Take input from the user  
    select = input("Please select operation -\n Add\n Subtract\n Multiply\n Divide\n") 
    
    num1 = int(input("Enter first number: ")) 
    num2 = int(input("Enter second number: ")) 
    
    if select == Add: 
        print(num1 + num2) 
    
    elif select == Subtract: 
        print(num1 - num2) 
    
    elif select == Multiply: 
        print(num1 * num2) 
    
    elif select == Divide: 
        print(num1 / num2) 
        
    else: 
        print("Invalid input") 

    print("\n\n\n\n")