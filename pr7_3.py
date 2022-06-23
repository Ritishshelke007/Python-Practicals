def add_item():
    stack_demo.append(add_element)
    print(stack_demo)

def display():
    print(stack_demo)

stack_demo = []
while True:
    choice = int(input("Select \n1. Add element in stack\n2. Remove elements from stack\n3. Display Stack\n4. Exit\n"))
    if(choice==1):
        add_element = int(input("Enter element to add : "))
        add_item()
        input()

    elif(choice==2):
        if(len(stack_demo)==0):
            print("cannot remove stack is empty!")
        else:
            stack_demo.pop()
            print("After removing element stack is : ",stack_demo)

    elif(choice==3):
        display()

    elif(choice==4):
        break
   
    

    
    


