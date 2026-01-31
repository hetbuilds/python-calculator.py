while True:
     op = input("Enter operation (+, -, *, / ,%, sq) or 'quit' to quit: ")

     if op == 'quit':
            print("Exiting the calculator. Goodbye!")
            break
     
     if op not in ['+', '-', '*', '/', '%', 'sq']:
        print("Invalid operation. Please try again.")
        continue
        
     if op not in ['sq']:
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
                result = num1 % num2
     else:
            num1 = float(input("Enter number to square: "))
            result = num1 ** 2

    

     print("The result is: {result}")              
                   