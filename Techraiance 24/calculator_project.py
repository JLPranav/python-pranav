def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if a!=0 :
        return a/b
    else:
        print("division not possible")
            
def calc():
    print("simple calculator")
    op = input("select operator \n + for addition \n - for subtraction \n * for multiplication \n / for division\n")
    a = float(input("enter num 1: "))
    b = float(input("enter num 2: "))
    
    if op == "+":
        print("result: ",add(a,b))
    elif op == "-":
        print("result: ",sub(a,b))
    elif op == "*":
        print("result: ",mul(a,b))
    elif op == "/":
        print("result: ",div(a,b))
    else:
        print("ivalid operator")
        
calc()

