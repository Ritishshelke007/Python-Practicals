import random

random_list = random.sample(range(1,101),20)
print(random_list)

occr = []
add_item = int(input("Enter a number to add last : "))
random_list.append(add_item)

num = int(input("Enter number to see its ocurences : "))

for i in range(len(random_list)):
    if random_list[i] == num:
        occr.append(i)

print("Number occured at indexes : ",occr)
        
        
		