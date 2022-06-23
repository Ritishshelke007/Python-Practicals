
# solution of 1 -->
print("solution of 1 -->")
multiples = 10,20,30,40,50,60,70,80,90,100
print("Multiples of 10 in tuple : ",multiples)


#solution of 2 -->
print("solution of 2 -->")
(a,b,c,d,e,f,g,h,i,j) = multiples
print("a : ",a)
print("b : ",b)
print("j : ",j)

#solution of 3 -->
print("solution of 3 -->")  
x,_,_,_,_,_,_,_,_,y = multiples
print(x,y,_)

#solution of 4 -->
print("#solution of 4 -->")
(x,*dis_var,y) = multiples
print("x : ",x)
print("disposal : ",dis_var)
print("y : ",y)