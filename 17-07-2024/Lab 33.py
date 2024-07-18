# Find whether a triangle is isoscles ->Two sides Equal ,
# equilateral-> all three sides  or
# scalene-> All sides are different

a = int(input("Enter the Value:"))
b = int(input("Enter the Value:"))
c = int(input("Enter the value:"))

if (a == b == c):
    print("This is Equilateral Triangle")
elif (a == b or a == c or b == c):
    print("This is isoscles Triangle")
else:
    print("This is scalene Triangle")
