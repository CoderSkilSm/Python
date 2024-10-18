 ls = [1,4,3,2]

 new = ls.sort()
print(new) # here .sort() does nothing instead it sorts the list in itslef.

print(ls) #here, we get the original sorted array

ls = [1,4,3,2]
new =sorted(ls) 

print(new) # returns the copy of the original list
print(ls) # returns the same as it is. 
