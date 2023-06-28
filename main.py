from art import logo

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}

def calc():
    print(logo)
    num1 = float(input("What is first number? "))
    for operators in operations:
        print(operators)
    should_continue = True 
    while should_continue:
        operator = input("Which Operator to choose from above ")
        num2 = float(input("What is next number? "))
        
        operation = operations[operator]
        ans = operation(num1, num2)
        print(f"{num1} {operator} {num2} = {ans}")
        further_calc = input(f"Type 'y' to continue calculating with {ans}, or type 'n' to start a new calculation: ").lower()
        if further_calc == "n":
            should_continue = False
            calc()
        else:
            num1 = ans


calc()
