startIndex = int(input('enter the starting index :'))
endIndex = int(input('enter the end index :'))
incrementBy = int(input('enter the value to increment :'))

if (startIndex > endIndex):
    print("starting index is greater than end index")
    
    for i in range(startIndex, endIndex, -incrementBy):  # -1 for reverse loop
        print("hello world", i)

elif (endIndex > startIndex):
    print("end index is greater than start index")
    
    for i in range(startIndex, endIndex, incrementBy):
        print("hello world", i)

    
else:
    print("Sorry, ur start and end index is same, So we cannot print anything.")
