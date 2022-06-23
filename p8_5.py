tup = ('F', 'I', 'a', 'b', 'b', 'e', 'r', 'g', 'a', 's', 't', 'e', 'd')
print("Tuple  = ", tup)

print("Solution of 1 -->")
tuple_update = list(tup)
tuple_update.append("!")
tup = tuple(tuple_update)
print("\Added element : ", tup)

print("Solution of 2 -->")
tup_string = ''.join(tup)
print("Conversion to String = ", tup_string)

print("Solution of 3 -->")
ext_list = []
for ele in tup:
    if ele=='b':
        ext_list.append(ele)

print("Extracted tuple = ", tuple(ext_list))

print("Solution of 4 -->")
print("Occurences of 'e' are : ", tup.count('e'))


print("Solution of 5 -->")
print("r is present in tuple ? = ", True if tup.count('r')>0 else False)

print("Solution of 6 -->")
print("Conversion to List = ", tuple_update)

print("Solution of 7 -->")
tuple_update.remove('b')
tuple_update.remove('e')
tuple_update.remove('r')
print("Updated tuple = ", tuple(tuple_update))
