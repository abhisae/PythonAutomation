# Find whether year is a leap year or not
# A leap year is divisible by 4 but not by 100 unless it is also divisible by 400

Year = int(input("Enter the Year:"))
if (Year % 4 == 0 and Year % 100!= 0):
    print("This is Leap Year")
elif (Year % 100 == 0 and Year % 400 == 0):
    print("This is Leap Year")
else:
    print("Not Leap Year")
