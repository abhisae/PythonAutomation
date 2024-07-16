#List Datatype with Function.

lst=[10,20,30,40,'a','b']

print(lst)
#method of List

#Len() :- It will return the lenghth of number in List
print("Lenght of the List:",len(lst))

#Count() - It will specified the number of occurances specified in the list
lst1=[1,1,2,2,2,5,6,6,7]
print(lst1.count(2))

#Index () - It retunrs the first occurance of specified item

lst2=[1,1,2,3,3,4,4,6,6,7]
print(lst2.index(3))

#Append() - We can use append() function to add item at the end of the list.
lst3=['A','B','C']
lst3.append('D')
print(lst3)

#Insert() -To insert item at specified index position
lst4=[1,2,3,4,5]
lst4.insert(0,99)
print(lst4)

#Extend() - To add all items of one list to another list
lst1=[1,2,3]
lst2=[4,5,6]
lst1.extend(lst2)
print(lst1)

#Remove() - We can use this function to remove specified item from the list.
# If the item present multiple times then only first occurrence will be removed.

lst5=[1,2,3,4,5,6,7,8,2]
lst5.remove(2)
print(lst5)

#pop() - It removes and returns the last element of the list.
lst6=[10,20,30,40,50]
lst6.pop()
print(lst6)

#reverse() - We can use to reverse() order of elements of list.
lst7=[10,20,30,40]
lst7.reverse()
print(lst7)

#sort() -In list by default insertion order is preserved.
# If want to sort the elements of list according to default natural sorting order then we should go for sort() method.

#For numbers ==>default natural sorting order is Ascending Order
#For Strings ==> default natural sorting order is Alphabetical Order

lst8=[20,5,1,67,99,1]
lst8.sort()
print(lst8)

lst11=['d','b','c','a','q','y']
lst11.sort()
print(lst11)

#copy - copy() function meant for cloning,Return the copy of the list.

lst9=[1,2,3]
lst10=lst9.copy()
print(lst10)

#Clear - For Clearing te List

lst12=[1,2,3,4,5,6,7,8]
lst12.clear()
print(lst12)
