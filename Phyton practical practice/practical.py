rows = int(input("Number: "))

for i in range(0,rows+1):
    for j in range(i):
        if i<10:
            print("0"+str(i), end="")
        else:
            print(i,end="")
    print()