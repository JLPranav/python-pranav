length=int(input("Enter the length (please enter the number without unit): "))
breadth=int(input("Enter the breadth (please enter the number without unit): "))
unit= input("Enter unit (please enter if it is cm,m,km, or any other unit): ")
area= length*breadth
area=str(area)
print("area:",area+"^2",unit)
l_b= length+breadth
perimeter= 2*l_b
print("perimeter :",perimeter,unit)
