#Sorting - Rearrange the elements in order
#[3,1,2,5,4] = [1,2,3,4,5] / [5,4,3,2,1]

mylist = [3,1,2,5,4]
mylist.sort(reverse = True)
print(mylist)
print(mylist.sort(reverse = False))

# Bubble sort
# Time Complexity - O(n^2)

mylist = [12,34,2,5,7]

for i in range(0, len(mylist)):
  for j in range(i, len(mylist)):
    if mylist[i] < mylist[j]:
        mylist[i],mylist[j] = mylist[j], mylist[i]

print(mylist)



# Insertion Sort
# Time Complexity - O(n^2)
mylist = [12,34,2,5,7]

for i in range(0, len(mylist)):
  minElement = 10000000
  minLocation = -1
  for j in range(i, len(mylist)):
    if minElement > mylist[j]:
      minElement = mylist[j]
      minLocation = j
      mylist[i],mylist[j] = mylist[j], mylist[i]


print(mylist)
