marks = int(input("Enter the marks:"))

if marks >= 50:
    print("Pass")
    if marks >= 75:
        print("Distinction")
    else:
        print("Average")
elif marks >=35:
    print("Good")
else:
    print("fail")