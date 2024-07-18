#Check if String is Palindrome or not

a= input("Enter the string you want compare:")
r=""
for i in a:
    r=i+r

if(a==r):
    print("String is Palindrome")
else:
    print("String is Not Palindrome")




