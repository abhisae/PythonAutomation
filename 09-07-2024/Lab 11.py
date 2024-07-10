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

#Count Method :- Find the Occurances present in string

s="Abhijit"
print("The count of i IS",s.count('i'))

#lower - Returns all in lowser case

txt = "Hello my FRIENDS"
s=txt.lower()
print(s)

#Upper - Retuns all in Upper Case

txt = "Hello my friends"
s=txt.upper()
print(s)

#endswith - This method returns "True" if specified value at the end
txt = "Hello my friends."
s=txt.endswith(".")
print(s)

#Startwith - This method return "True" if specified Value at the start
txt = "Hello my friends."
s=txt.startswith("Hello")
print(s)

#capitalize :- This method returs the First charcher in Uppercase rest all in lowser case

txt = "hello, and welcome to my World."
s=txt.capitalize()
print(s)

txt = "hELLO, AND WELCOME TO MY WORLD."
s=txt.capitalize()
print(s)

#Center :- Align string in Center

txt='Python'
s=txt.center(20,"O")
print(s)

#Replace : It replaces the Old character to the new character. It requires 2 Arguments( Old, New)

s="Python"
x=s.replace('P','J')
print(x)

#format():-The format() method formats the specified value(s) and insert them inside the string's placeholder.
#the placeholder is defined using curly brackets: {}.

#Named Index
txt1 = "My name is {name}, I'm {age}".format(name = "python", age = 1979)
print(txt1)

#Number Index
txt1 = "My name is {0}, I'm {1}".format("python",  1979)
print(txt1)

#Empty Placeholder
txt1 = "My name is {}, I'm {}".format("python", 1979)
print(txt1)


#isalnum():--returns True if all the characters are alphanumeric,
# meaning alphabet letter (a-z) and numbers (0-9).

#eg.1
txt="Python123"
b=txt.isalnum()
print(b)  #o/p ->True

#eg.2
txt="Python@123"
b=txt.isalnum()
print(b)  #o/p ->False

#eg.3
txt="Python_123"
b=txt.isalnum()
print(b)  #o/p -False


#istitle():-- returns True if all words in a text start with a upper case letter,
# AND the rest of the word are lower case letters, otherwise False.

txt="Python12"
b=txt.istitle()
print(b)  #O/P ->True

txt="python12"
b=txt.istitle()
print(b)  #o/p ->False

txt="PYTHON12"
b=txt.istitle()
print(b) #o/p ->False

txt="Python 12"
b=txt.istitle()
print(b)  #o/p ->True
