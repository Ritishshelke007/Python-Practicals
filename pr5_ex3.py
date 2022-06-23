from string import digits


string = input("Enter an Alphanumeric string : ")
no_alpha = no_dig =  0
alphabets = []
digits = []

for i in range(len(string)):
    if(string[i].isalpha()):
        alphabets.append(string[i])
        no_alpha = no_alpha + 1
    elif(string[i].isdigit()):
        digits.append(string[i])
        no_dig = no_dig + 1

print("Alphabets in String : ",alphabets)
print("Number of Alphabets in String :  ", no_alpha)
print("Digits in String : ",digits)
print("Number of Digits in String :  ", no_dig)
