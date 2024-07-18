#List Comprehension :-
#List comprehension offers a shorter syntax
# when you want to create a new list based on the values of an existing list.


fruits=['banana','apple', 'mango','cherry','lime','mosambi']
new_fruits=[x for x in fruits if "m" in x]
print(new_fruits)

#Accepts only number lower than five
lst=[1,4,10,20]
lst1=[x for x in lst if x<=5 ]
print(lst1)

#Convert to Upper case in list
newlist1=[x.upper() for x in fruits]
print(newlist1)