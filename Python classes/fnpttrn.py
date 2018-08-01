
    



def star1():
    for i in range(1, 4):
        for j in range(0, i):
            print(j+1, end="")
        print("")


def star2():
    for i in range(4, 0, -1):
        for j in range(1, i, +1):
            print("*", end=" ")
        print(" ")
try:
    value = int(input('Enter a value to print patterns:'))
    if (value==2):
        star2()
    elif (value==1):
        star1()
    else:
        print("Enter between 1 and 2")


except ValueError:
    print("Sorry, Enter integer value only")
    
    













    
