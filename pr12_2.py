

def factorial(num):
    i = 1
    fact = 1

    for i in range(1,num+1):
        fact = fact*i
        
    return fact

number = int(input("Enter a number to find a factorial: "))
res = factorial(number)
print("Factorial of "+ str(number) + " is: "+ str(res))