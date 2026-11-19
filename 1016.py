name = input("Enter student name:")
marks = int(input("Enter your marks:"))

if marks < 0 or marks > 100:
    print("Invalid marks")

else :
    if marks >= 90:
        grade = "A"
    elif marks >= 80:
        grade = "B"
    elif marks >= 70:
        grade = "C"
    elif marks >= 60:
        grade = "D"
    elif marks >= 50:
        grade = "E"
    else :
        grade = "Fail"

        print("\n===========Result============")
        print("Name : ", name)
        print("Marks :", marks)
        print("Grade:", grade)
        print("==============================")