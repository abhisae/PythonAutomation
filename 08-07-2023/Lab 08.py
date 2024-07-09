# Find out even and odd numbers
#a=5

#if (a%2==0):
#    print("a is even number")
#    print("a is odd number")


# Find the even and Odd Number by using input function4

a=int(input("Enter the number"))
if(a%2==0):
    print("a is even number")
else:
    print("a is odd number")

#Addition of two numbers

a=int(input("Enter first Number:"))
b=int(input("Enter second Number:"))

c=sum([a,b]) # This is using list also we can use Tuple sum((a,b))
print("Addition is:",c)
