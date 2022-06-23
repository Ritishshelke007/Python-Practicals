#Question 1 

quantity = int(input('Enter value of quantity: '))
price = float(input('Enter value of price: '))

if(quantity>1000):
    discount = 10
    print("10% Discount Applied!")

else:
    discount = 0
    print("Discount available only for Quantity greater than 1000!")
        
dis = quantity * price * discount / 100

expense = quantity * price - dis
print("--------------------------------")
print("Your Total Expenses : ",expense);
print("--------------------------------")       


