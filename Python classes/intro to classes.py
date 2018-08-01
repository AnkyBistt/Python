class Student:
    studentName = ""
    studentAddress = ""


    def __init__(self):    #its how a constructor is defined in python inside a class
        print("Halo YOu are in class")
        self.takeUserInput()
        print(self.studentName, self.studentAddress)
        


    def takeUserInput(self): #self keyword to reference the class functions and variable
        self.studentName = input("Enter the Student's Name.")
        self.studentAddress = input("Enter the student's address.")
        
       #print(userName, address)


        
obj = Student()


