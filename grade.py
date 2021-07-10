# Write a program to compute the grade from marks.

marks = int(input("Enter the marks you obtained: "))

if(marks<=50):
    print("You obtained {} marks which is grade F".format(marks))
elif(marks>  50 and marks<=60):
    print("You obtained {} which is grade E".format(marks))
elif(marks>  60 and marks<=70):
    print("You obtained {} which is grade D".format(marks))
elif(marks> 70 and marks<=80):
    print("You obtained {} which is grade C".format(marks))
elif(marks>  80 and marks<=90):
    print("You obtained {} which is grade B".format(marks))
elif(marks>  90 and marks<=100):
    print("You obtained {} which is grade A".format(marks))

