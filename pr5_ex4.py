
num = int(input("Enter a 5 digit number : "))
rev = 0
original = num

while(num>0):
    rev = (rev*10)
    rev = num%10 + rev
    num = num//10

print("Reverse of given number is : ",rev)

if(original == rev):
    print("Given Number and Reverse number are equal")
else:
    print("Given Number and Reverse number are different")