


while True:
     op = input("Enter operation (+, -, *, / ,%, sq, sqroot, area) or 'quit' to quit: ")

     if op == 'quit':
            print("Exiting the calculator. Goodbye!")
            break
     
     if op not in ['+', '-', '*', '/', '%', 'sq', 'sqroot', 'area']:
        print("Invalid operation. Please try again.")
        continue
        
     if op not in ['sq', 'sqroot', 'area']:
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

     elif op == 'area':
            
          
            shape = input("Enter shape (circle, rectangle, triangle): ")
            if shape == 'circle':
                radius = float(input("Enter radius: "))
                import math
                result = math.pi * radius ** 2
                appresult = 22/7 * radius ** 2
                print(f"The area of the circle using approximate value of pi (22/7) is: ~{appresult}")
                print(f"The area of the circle using exact value of pi is: ~{result}")
            elif shape == 'rectangle':
                length = float(input("Enter length: "))
                width = float(input("Enter width: "))
                result = length * width
            elif shape == 'triangle':
                base = float(input("Enter base: "))
                height = float(input("Enter height: "))
                result = 0.5 * base * height
            else:
                print("Invalid shape. Please try again.")
                continue 
                    
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
                   