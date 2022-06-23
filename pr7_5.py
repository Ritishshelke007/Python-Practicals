import random

random_list = random.sample(range(10,100),20)
print(random_list)

list = random_list

print("List after deleting numbers between 20 and 50")
for i in (list):
    if(i>=20 and i<=50):
        list.remove(i)
    else:
        print(i,end=' ')


