import random
import string

a = string.ascii_letters+string.digits+string.punctuation[:1]+string.punctuation[2:6]+string.punctuation[21:22]+string.digits

c = ""
for i in range(int(4)):
    d = random.randrange(len(a))
    c+=a[d]
print(c)

inp = input("Enter OTP: ")

if inp == c:
    print("Access Granted")
else:
    print("Invalid OTP")