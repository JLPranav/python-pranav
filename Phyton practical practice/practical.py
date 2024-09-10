num = input("Num: ")
sum = 0
for i in range(0,len(num)):
    sum += int(num[i])**3
if sum==int(num):
    print("amstrong")
else:print('amweak')