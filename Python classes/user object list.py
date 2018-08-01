class Data:
    name= ""
    age = 0
    phone = 0



    def __init__(self, name, age, phone):
        self.name = name
        self.age = age
        self.phone = phone


objList = []
entries = int(input('Enter the no. of entries you want to make: '))


for i in range(0,entries):
    print("Enter the details of student:")
    name = input('Enter the name of student:-> ')
    age = int(input('Enter the age of student:-> '))
    phone = int(input('Enter the phone no. of student:->'))

    obj = Data(name,age,phone)
    objList.append(obj)








for item in objList:
    print("Name is",item.name)
    print("Age is", item.age)
    print("Phone no. is:",item.phone)
