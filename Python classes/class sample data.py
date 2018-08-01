class SampleData:
    name = ""
    age = ""
    phone = ""



    def __init__(self, name, age, phone):
        self.name = name
        self.age = age
        self.phone = phone


    def displaydata(self):
        print("Name is:", self.name)
        print("Age is:", self.age)
        print("Phone is:", self.phone)

objList = []

obj = SampleData("Ranu",21,2873)
obj1= SampleData("Ankit", 21, 7895)
obj2 = SampleData("vijay", 21, 97883)

objList.append(obj)
objList.append(obj1)
objList.append(obj2)
#obj.displaydata()


for item in objList:

    print("Name is:", item.name)
    print("Age is:", item.age)
    print("Phone is:", item.phone)

