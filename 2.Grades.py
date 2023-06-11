def gr(grades):
    if 2.00 <= grades <= 2.99:
        print("Fail")
    elif 3.00 <= grades <= 3.49:
        print("Poor")
    elif 3.50 <= grades <= 4.49:
        print("Good")
    elif 4.50 <= grades <= 5.49:
        print("Very Good")
    elif 5.50 <= grades <= 6.00:
        print("Excellent")


grade = float(input())
gr(grade)



