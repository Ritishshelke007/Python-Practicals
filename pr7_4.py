queue_demo = []

while True:
    choice = int(input("Select \n1. Add element in Queue\n2. Remove elements from Queue\n3. Display Queue\n4. Exit\n"))

    if(choice==1):
        add_item = int(input("Enter element to add : "))
        queue_demo.append(add_item)
        print("After adding Queue is : ",queue_demo)
        input()

    elif(choice==2):
        if(len(queue_demo)==0):
            print("cannot remove queue is empty!")
        else:
            queue_demo.pop(0)
            print("After removing element queue is : ",queue_demo)
        

    elif(choice==3):
        print(queue_demo)

    elif(choice==4):
        break

    
