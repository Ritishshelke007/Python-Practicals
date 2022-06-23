
import random


#Question 1
s = {10,2,-3,4,5,88}
print('Question 1')
#1. no of items in set
print('Number of items in set are : ',len(s))
#2 3. maximum & minimum elements in set s
print('Maximum element in set : ',max(s))
print('Minimum element in set : ',min(s))
#4 . sum of all elements in set s
print('Sum of all elements in set : ',sum(s))
#5. obtain a new sorted set from set s, set s remaining unchanged
s2 = sorted(s)
print('Sorted set : ',s2)
#6. report whether 100 is an element of set s 
msg = '100 is present in set' if 100 in s else '100 not in set'
print(msg)
#7. report whether -3 is an element of set s
msg = '-3 is present in set' if -3 in s else '-3 is not in set'
print(msg)
print('----------------------------------')

print('Question 2')
names = {'Ayush','Atharv','Ritish','Aradhya','Bala','Bhuvi'}
set_of_A = set()
set_of_B = set()
not_A_B = set()

for i in names:
    if i.startswith('A' or 'A'):
        set_of_A.add(i)
    elif i.startswith('B' or 'b'):
        set_of_B.add(i)
    else:
        not_A_B.add(i)


print('Names starts with A : ',set_of_A)
print('Names starts with B : ',set_of_B)
print('Names that not starts with A or B : ',not_A_B)
print('--------------------------------------------')

print('Question 3')
names2 = set()
names2.update(['Ritish','Omkar','Jiyan','Vinayak','Prasad'])
print('New Set : ',names2)
#modifies existing name 
names2.remove('Ritish')
names2.add('RITISH')
print('After modifying Ritish : ',names2)

#deleting 
names2.discard('Prasad')
names2.remove('Omkar')
print('After removing some elemets : ',names2)
print('-------------------------------------------')

print('Question 4')
#10 randomly generated numbers in the range 15-45
random_nos = set()
for i in range(10):
    random_nos.add(random.randint(15, 45))
print(random_nos)
#count how many of this numbers are less than 30 delete all numbers which are greater than 35
count = 0
t = set()
for j in random_nos:
    if j < 30:
        count += 1
    if j <= 35:
        t.add(j)

random_nos = t

    

print('Nos less than 30 are : ',count)
print('Set after deleting nos greater than 35 :',random_nos)
print('-----------------------------------------------------')
#Question 6
set3 = {'mango','banana','apple','kiwi'}
set3.clear()
print(set3)
#del(set3)
print(set3)
print('------------------------------------------------')

print('Question 7')
s1 = ()
s2 = {}
print(type(s1))
print(type(s2))
