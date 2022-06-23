
nos = [74,56,-36,55,-87,-12]
positive_nos = []
negative_nos = []

for i in nos:
    if(i<0):
        negative_nos.append(i)
    else:
        positive_nos.append(i)
        
print("Original list : ",nos)
print("Negative numbers in the list : ",negative_nos)
print("Positive numbers in the list : ",positive_nos)