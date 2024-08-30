import string
import random
b = input("Enter length: ")
a = string.ascii_letters+string.digits+string.punctuation[:1]+string.punctuation[2:6]+string.punctuation[21:22]
c = ""
for i in range(int(b)):
    d = random.randrange(len(a))
    c+=a[d]
print(c)