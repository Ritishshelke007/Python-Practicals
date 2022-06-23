# Python program to display all the prime numbers within an interval



#print("Prime numbers between", lower, "and", upper, "are:")

for num in range(1, 300):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)