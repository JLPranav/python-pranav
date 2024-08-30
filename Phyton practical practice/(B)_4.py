days = {1:"Sunday",2:"Monday",3:"Tuesday",4:"Wednesday",5:"Thursday",6:"Friday",7:"Saturday"}
x = True
while x:
    day = int(input("Please enter a number between 1 and 7: "))
    if day<8:
        print(days[day])
        x = False
    else:
        print("Invalid input. Please enter a number between 1 and 7.")