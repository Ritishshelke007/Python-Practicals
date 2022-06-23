#create a list of 5 odd numbers
from cgi import print_directory


odd = [23,55,71,97,63]
#create a list of 5 even numbers
even = [62,58,14,2568,1034]
#combine two list
odd.extend(even)
print("Combined list : ",odd)
#add prime numbers at beginning 
odd.insert(0,11)
odd.insert(1,17)
odd.insert(2,29)
print("After adding prime numbers : ",odd)
#report how many elements are in list
print("Length of list : ",len(odd))
#replace last three numbers in the list
odd[10:] = [100,200,300]
print("After replacing last 3 numbers : ",odd)
#delete all numbers in list
odd.clear();
print("After deleting all numbers in list : ",odd)
#delete the list
del odd
print("List deleted now : ",odd)