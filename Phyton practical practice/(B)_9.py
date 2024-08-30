p = int(input("Cost of your bike: "))
percentile = 0
if p>100000:
    percentile = 15
elif p>50000 and p<=100000:
    percentile  = 10
elif p<=50000:
    percentile = 5
    
tax = (percentile/100)*p
print("Tax is",str(tax)+"Rs")