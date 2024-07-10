#String Datatype

s="durga goddess"
print(s[0])
print(s[5])
print(s[12])
print(s[-1])
print(s[-7])
print(s[-8])
print(s[-9])

#Methods of String
#1.Length

a=len(s)
print("Lenght of the string is:",a)

# a=len(s[14])
# print("Lenght of the string is:",a) -->After executing this program will get erroe message "String Index out of Range"


#2.Find

b=s.find('s') #it will return first occurance of the location of character
print(b)

# b=s.find('z') #In this case it will return the -1 because 'z' is not in string.
# print(b)


#Join
a='P'
b='Automation'.join(a)
print(b)

#Strip --> It is used to remove the white spaces at the begining and end of the string
txt = "     welcome to the class    "
print(txt.strip())

print(txt.strip(s)) # Here if we give the s character then why it is removing ass from the word Class

#Split method :- Split string into List
txt = "     welcome to the class    "
x=txt.split()
print(x)

#Zfill method :- The zfill() method adds zeros (0) at the beginning of the string, until it reaches the specified length.
# If the value of the len parameter is less than the length of the string, no filling is done.

a="Hello"
print(a.zfill(10))
print(a.zfill(4))
