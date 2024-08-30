# define a function called bmi_calculator
def bmi_calculator(height,weight):
    # return weight divided by height squared
	return weight/(height*height)

# declare a variable called "result" and
# assign it the result of using the function
# use height = 1.69 and weight = 69
result = bmi_calculator(1.75,75)

# print the "result" variable
print(result)