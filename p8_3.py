names = [("Ritish",),"Prerna","Pooja",("Omkar",),("Prasad",),("Vinayak",)]
Boys = 0
Girls = 0
for i in names:
    if isinstance(i,tuple):
        Boys += 1
    else:
        Girls += 1

print("Boys: ",Boys,"\nGirls: ",Girls)
print("Total students: ",Boys+Girls)