a = input("word: ")
b = []

for i in a:
    if i == "a" or i == "e" or i == "o" or i == "i" or i == "u":
        continue
    else:
        print(i,end=" ")