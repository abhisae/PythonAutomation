#Python program to interchange first and last elements in a list

lst1=[20,10,5,7]
a=lst1[0]
lst1[0]=lst1[-1]
lst1[-1]=a
print(lst1)

#Another Logic as Below
newList = [12, 35, 9, 56, 24]
first = newList.pop(0)
last = newList.pop(-1)
newList.insert(0, last)
newList.append(first)
print((newList))


a='hello'

