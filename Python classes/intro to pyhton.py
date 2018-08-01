#variables in python are declared without data type

##firstNumber = 10   #variable-name = value
##secondNumber = 30  #variable-name = value

firstNumber = int(input('enter first no.'))
secondNumber = int(input('enter second no.'))

result = firstNumber * secondNumber


# we use print function to print any output
#when we have to print a string and another datatype then first we have to convert into string datatype using str() function
#to convert it only while displaying.
#print("multiplication of two number is:" + str(result))


print("mul of two number i.e %d and %d is : %d" %(firstNumber, secondNumber, result))



print("Mul of two numbers i.e", firstNumber, "and", secondNumber, "is:", result)
