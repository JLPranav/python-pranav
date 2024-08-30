def Q1():
    print("Question 1")
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    c = int(input("Enter the third number: "))
    sum_numbers = a + b + c
    product_numbers = a * b * c
    print("The sum of the numbers is: ", sum_numbers)
    print("The product of the numbers is: ", product_numbers)
    return sum_numbers, product_numbers

def Q2():
    print("Question 2")
    n = int(input("Number: "))
    Fact = 1
    i = 1
    while i <= n:
        Fact *= i
        i += 1
    print("Factorial:", Fact)

def Q3():
    print("Question 3")
    side1 = float(input("Enter the length of side 1: "))
    side2 = float(input("Enter the length of side 2: "))
    side3 = float(input("Enter the length of side 3: "))

    if side1 == side2 == side3:
        print("Equilateral Triangle")
    elif side1 == side2 or side1 == side3 or side2 == side3:
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")
        
def Q4():
    print("Question 4")
    km = float(input("Enter distance in kilometers: "))
    miles = km * 0.621371
    print(f"{km} kilometers is equal to {miles} miles.")
    
def Q5():
    print("Question 5")
    distance = float(input("Enter distance traveled (in kilometers): "))
    time = float(input("Enter time taken (in hours): "))

    speed = distance / time

    print(f"The speed of the vehicle is {speed} kilometers per hour.")

def Q6():
    print("Question 6")
    number = int(input("Enter a number: "))
    
    i = 1
    while i <= 10:
        product = number * i
        print(f"{number} x {i} = {product}")
        i += 1

def Q7():
    print("Question 7")
    name = input("Enter employee name: ")
    age = int(input("Enter employee age: "))
    basic_salary = float(input("Enter basic salary: "))

    da = 0.10 * basic_salary
    hra = 0.10 * basic_salary

    total_salary = basic_salary + da + hra

    print(f"\nEmployee Details:")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Basic Salary: {basic_salary}Rs")
    print(f"DA (10%): {da}Rs")
    print(f"HRA (10%): {hra}")
    print(f"Total Salary: {total_salary}Rs")
    
def Q8():
    print("Question 8")
    year = int(input("Enter a year: "))

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")

def Q9():
    print("Question 9")
    age = int(input("Enter your age: "))

    if age >= 18:
        print("You are a valid voter.")
    else:
        print("You are not eligible to vote yet.")
        
def Q10():
    print("Question 10")

    start_range = int(input("Enter the starting range: "))
    end_range = int(input("Enter the ending range: "))

    for number in range(start_range, end_range + 1):
        if number % 7 == 0 and number % 5 == 0:
            print(number)

def Q11():
    print("Question 11")
    print("Enter the range for fizzbuzz:")
    start_range = int(input("Enter the starting range: "))
    end_range = int(input("Enter the ending range: "))

    for number in range(start_range, end_range + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("fizzbuzz")
        elif number % 3 == 0:
            print("fizz")
        elif number % 5 == 0:
            print("buzz")
        else:
            print(number)
            
def Q12():
    print("Question 12")
    limit = int(input("Enter the number of natural numbers to print: "))
    count = 1

    while count <= limit:
        print(count)
        count += 1
    
def Q13():
    print("Question 13")
    units = int(input("Enter the number of units: "))

    if units <= 100:
        total_bill = units * 3
    elif units < 200:
        total_bill = (100 * 3) + ((units - 100) * 5)
    else:
        total_bill = (100 * 3) + (100 * 5) + ((units - 200) * 10)

    print(f"The total electricity bill is Rs. {total_bill}")

def Q14():
    print("Question 14")
    percentage = float(input("Enter the percentage: "))

    if percentage > 90:
        grade = 'A'
    elif 75 <= percentage <= 90:
        grade = 'B'
    elif 55 <= percentage < 75:
        grade = 'C'
    elif 40 <= percentage < 55:
        grade = 'D'
    else:
        grade = 'F'

    print(f"The grade for {percentage}% is: {grade}")

def Q15():
    print("Question 15")
    name = input("Enter a name: ")

    i = 0
    while i < len(name):
        print(name[i])
        i += 1

# Q1()
# Q2()
# Q3()
# Q4()
# Q5()
# Q6()
Q7()
# Q8()
# Q9()
# Q10()
# Q11()
# Q12()
# Q13()
# Q14()
# Q15()