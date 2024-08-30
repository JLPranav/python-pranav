co1 = input("Coordinates of point 1: ")
x1,y1 = tuple(co1.split(",",3))
co2 = input("Coordinates of point 1: ")
x2,y2 = tuple(co2.split(",",3))
xm = (int(x1)+int(x2))/2
ym = (int(y1)+int(y2))/2
print(x1,y1,x2,y2,xm,ym)
print("Midpoint = "+str(xm)+","+str(ym))