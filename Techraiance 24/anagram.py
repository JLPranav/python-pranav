#peach/cheap stop/pots arc/car state/taste
# a = input("word1: ")
# b = input("word2: ")
def my1(a,b):
    l = []
    count = 0
    if len(a)==len(b):
        for i in a:
            for g in range(0,len(a)):
                if i==b[g]:
                    l.append(True)
    for i in l:
        if i == True:
            count+=1
    if count==len(a):
        # print("is anagram")
        return True
    else:
        # print("not anagram")
        return False
        
def my2(a,b):
    if sorted(a.lower()) == sorted(b.lower()):
        print("is anagram")
    else:
        print("not anagram")
        
# my2(a,b)

