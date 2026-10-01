import art
def add(n1,n2):
    return n1 + n2
def subtract(n1,n2):
    return n1 - n2
def multiply(n1,n2):
    return n1 * n2
def divide(n1,n2):
    return n1 / n2
operation={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide

}
def calculator():
    print(art.logo)
    should_continue_calculate=True
    num1=float(input("Enter the first number: ")) 
    while should_continue_calculate:
        for symbol in operation:
            print(symbol)
        symbol=input("Select symbol: ")
        num2=float(input("Enter the second number: "))
        answer=operation[symbol](num1,num2)
        print(f"{num1} {symbol} {num2} = {answer}")
        choice=input(f"Type 'y' to continue calculation with {answer}, or type 'n' to start a new calculation: ").lower()
        if choice=="y":
            num1=answer
            
        else:
            should_continue_calculate=False
            print("\n"*20)
            calculator()
calculator()