class Student:
    num1 = ""
    num2 = ""


    def __init__(self):    #its how a constructor is defined in python inside a class
        self.mul()
       
        


    def mul(self): #self keyword to reference the class functions and variable
        self.num1 = int(input('Enter the first no.'))
        self.num2 = int(input('Enter the second no.'))
        result = self.num1 * self.num2
        print("Multiplication", result)
        
       #print(userName, address)


        
obj = Student()



