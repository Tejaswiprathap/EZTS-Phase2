queue=[]
def enqueue():
    if len(queue)==n:
        print("Queue is full!")
    else:
        element=input("Enter the element for queue: ")
        queue.append(element)
        print(queue)
def dequeue():
    if not queue:
        print("Queue is empty, add the element: ")
    else:
        e=queue.pop(0)
        print(e," removed")
        print(queue)

n=int(input("Enter size of the queue: "))
while True:
    print("Select the operation 1.enqueue 2.dequeue 3.exit ")
    choice=int(input())
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        break
    else:
        print("Enter the correct operation!")
