# define a function called reverseString that takes in one argument
def reverseString(str):
# declare a variable with an empty string
    nstr = ""
# declare a variable containing the length of the string
    lenght = len(str)
# loop through a range function, where the first argument is 1 and second argument is length of the string (second variable) plus one
    for i in range(1,lenght+1):
# get the negative index of the string, and add it to the first variable
        nstr+=str[i*-1]
# print the first variable
    print(nstr)

# test cases
reverseString("Python")
reverseString("Hello world")
reverseString("Foobar")