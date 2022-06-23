print("Program to demonstrate function with minimum 2 arguments.")
print("---------------------------------------------------------")

def CalculateMortage(amt, intr, months):
    mortage = amt * (intr * (1 + intr)** months) / ((1 + intr) ** months - 1)
    print(mortage)

amount = int(input("Enter the amount of loan: "))
intrest = int(input("Enter the intrest rate: "))
intrest = float(intrest) / 100 / 12
months = int(input("Enter the number of months: "))
CalculateMortage(amount, intrest, months)
