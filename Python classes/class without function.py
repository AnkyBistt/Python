class Student:
    studentName = ""
    studentAddress = ""


    def __init__(self, studentName, studentAddress):    #its how a constructor is defined in python inside a class
        print("Halo YOu are in class")
        self.studentName = studentName
        self.studentAddress = studentAddress
        print(self.studentName, self.studentAddress)
        

studentName =input("Enter ur name: ")
studentAddress = input("Enter ur address: ")


        
obj = Student(studentName, studentAddress)



