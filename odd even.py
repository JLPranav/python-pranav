even = []
odd = []
import time
b = input("Enter number: ")

for i in range(int(b)):
    i = i+1
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)
print("Even:", end=" ")
for a in even:
    print(a, end=" ")
    time.sleep(0.5)
print()
print("Odd:", end=" ")
for a in odd:
    print(a, end=" ")
    time.sleep(0.5)
print()

