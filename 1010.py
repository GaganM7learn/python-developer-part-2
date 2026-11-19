number = int(input("Enter a number:"))

if number % 2 == 0 :
    print( number , "its an Even number")
    if number < 0 :
        print("Negative number")
    elif number > 0 :
        print("Positive number")

    elif number == 0 :
        print("Zero")

else :
    print(number , "is an odd number")

    if number < 0 :
        print("Negative number")

    elif number > 0 :
        print("Positive number")

    elif number == 0 :
        print("Zero")