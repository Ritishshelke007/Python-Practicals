import operator
import matplotlib.pyplot as plt

print('Question 1')
students = {'Ritish':19,'Omkar':18,'Jiyan':22}
#copy into stud
stud = students.copy()
#empty the students dictionary
students.clear()
print('stud :',stud)
print('students :', students)
print('--------------------------------------')
print('Question 2')
list1 = ['Rohit','Shikhar','Virat','DK','MSD','Harshal']
#using list to create dictionary
dict1 = dict.fromkeys(list1,50)
print(dict1)
print('--------------------------------------')
print('Question 3')
marks = {'Anurag':96,'Raj':99,'Prasad':85,'Rahul':74}
print('Original Dictionary : ',marks)
#sorting with key
marks1 = sorted(marks.items())
print('Ascending order via key : ',marks1)
marks2 = sorted(marks.items(),reverse=True)
print('Descending order via key : ',marks2)
#sorting with value
marks1 = sorted(marks.items(),key=operator.itemgetter(1))
print('------------------')
print('Ascending order via Value : ',marks1)
marks2 = sorted(marks.items(),key=operator.itemgetter(1),reverse=True)
print('Descending order via Value : ',marks2)
print('---------------------------------------------------------')
print('Question 4')
dict1 = {'Rohit':'India','Rahul':'US'}
dict2 = {'Umesh':'UK','Kartik':'Oman'}
dict3 = {'Swati':'India','Mrunal':'France'}
#
dict4 = {**dict1,**dict2,**dict3}
print('Dictionary 1 : ',dict1)
print('Dictionary 2 : ',dict2)
print('Dictionary 3 : ',dict3)
print('Concatenated Dictionary :',dict4)
print('-----------------------------------------')
print('Question 5')
dict3.clear()
if not bool(dict3):
    print('Dictionary dict2 is Empty')
print('------------------------------------------')
print('Question 6')
d = {
    'anuj':{'salary':10000,'age':20,'height':6},
    'aditya': {'salary': 6000, 'age': 26, 'height': 5.6},
    'rahul': {'salary': 7000, 'age': 26, 'height': 5.9},
}
lst = []
for v in d.values():
    lst.append(v['salary'])
print('maximum salary : ',max(lst))
print('minimum salary : ',min(lst))
print('-----------------------------------------')
print('Question 7')
stud = {115:'Ritish',116:'Vinayak',111:'Siddharth'}
roll_no = int(input('Enter roll number : '))
name = stud.get(roll_no,'Student')
print(f'Congratulations {name}!!!')
print('-------------------------------------------')
print('Question 8')
string = str(input('Enter a string : '))
freq = {}

for i in string:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print(string)

print('Count of characters in string : ',str(freq))
plt.hist(freq)

print('----------------------------------------------')
print('Question 9')
marks = {
    'Subu':{'Maths':88,'Eng':60,'SSt':95},
    'Amol': {'Maths': 78, 'Eng': 68, 'SSt': 89},
    'Raka': {'Maths': 56, 'Eng': 66, 'SSt': 77},
}
print("Amol's English Marks : ",marks['Amol']['Eng'])
marks['Raka']['Maths'] = 77
print('Updated Marks : ',marks)



