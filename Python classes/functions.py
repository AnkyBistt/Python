#function without argument

##def functionName():
##    print("Hello world!")
##
##functionName()



# function that return a value
##def sum(firstNumber, secondNumber):
##    thirdNumber = firstNumber + secondNumber
##    return thirdNumber
##
##
##result = sum(10, 20)
##print(result)





def call(userName, firstNumber, secondNumber):
    result = firstNumber + secondNumber
    print("Hello " ,  userName ,"!", "the sum of" , firstNumber, "and", secondNumber, "is:", result)



userName = input('Enter Your Name:')
try:
    firstNumber = int(input('Enter the first no.: '))
    secondNumber = int(input('Enter the second no.:'))
    call(userName, firstNumber, secondNumber)

except ValueError:
    print("sorry, Enter only integer value")
