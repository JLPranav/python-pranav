from math import pow
pi = 22/7
r= input("Enter radius(without unit): ")
r=float(r)
a= pi*pow(r,2)
a= str(a)
unit=input("Enter unit: ")
a= a+"sq"+unit
curcumflerence= 2*pi*r
curcumflerence= str(curcumflerence)+unit
print("Curcumflerance: ",curcumflerence)
print("Area: ",a)
