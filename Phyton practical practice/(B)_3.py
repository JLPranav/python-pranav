s1 = int(input("Side 1: "))
s2 = int(input("Side 2: "))
s3 = int(input("Side 3: "))
if s1==s2==s3:
    print("Equilateral")
elif (s1==s2!=s3) or (s1!=s2==s3) or (s1==s3!=s2):
    print("Isosceles")
else:
    print("scalene")