d = True
while d:
    a = int(input("Enter number: "))
    b = 0
    for i in range(2, a):
        # print(a,"%",i,"=",a%(i))
        if a % i == 0:
            print("Not Prime")
            break
    else:
        print("Is Prime")

    c = input("Do you want to continue(Y/N): ")
    if c != "Y":
        if c != "y":
            if c != "Yes":
                if c != "yes":
                    break