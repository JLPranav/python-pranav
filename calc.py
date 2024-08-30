while True:
    expression = input("Enter Expression\n")
    if expression == "":
        break
    print("Result is: ", eval(expression),"\n")
