while True:
     op = input("Enter operation (+, -, *, / ,%, sq, sqroot) or 'quit' to quit: ")

     if op == 'quit':
            print("Exiting the calculator. Goodbye!")
            break
     
     if op not in ['+', '-', '*', '/', '%', 'sq', 'sqroot']:
        print("Invalid operation. Please try again.")
        continue
        
     if op not in ['sq', 'sqroot']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            if op == '+':
               result = num1 + num2       
            elif op == '-':
                result = num1 - num2
            elif op == '*':
                result = num1 * num2
            elif op == '/':
                if num2 == 0:
                     print("Error: Division by zero is not allowed.")
                     continue
                result = num1 / num2
            elif op == '%':
                if num2 == 0:
                     print("Error: Division by zero is not allowed.")
                     continue
                result = num1 / num2 * 100
     else:
            if op == 'sqroot':
                import math
                num1 = float(input("Enter number to find square root: "))
                if num1 < 0:
                    print("Error: Cannot compute square root of a negative number.")
                    
                result = math.sqrt(num1)
            elif op == 'sq':
                 num1 = float(input("Enter number to square: "))
                 result = num1 ** 2

    
     print(f"The result is: {result}")        

                   
