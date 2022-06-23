nos = []
dup_no = []

print("Enter element in list which contains some duplicates : ")

for i in range(10):
    item = int(input())
    nos.append(item)

print("Items in the list : ",nos)    

for i in nos:
    if i not in dup_no:
        dup_no.append(i)

print("List after removing duplicate elements : ",dup_no)