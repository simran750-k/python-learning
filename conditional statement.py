#wap to check the grade of student by taking the input from the users
marks = int(input("enter the marks of student"))
print("entered marks :",marks)
if(marks>90):
    print("a+")
elif(90>marks and marks>80):
    print("a")
elif(80>marks and marks>70):
    print("b+")
else:
    print("fail")
