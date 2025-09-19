class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self,item):
        self.queue.append(item)
        print(f"Enqueued : {item}")
    def dequeue(self):
        if len(self.queue) > 0:
            item = self.queue.pop(0)
            print(f"Dequeued : {item}")
        else:
            print("Queue is empty")
q = Queue()
n = int(input("Enter the number of elements : "))
for i in range(n):
    q.enqueue(input("Enter the element : "))
print(q.queue)
q.enqueue(250)
print(q.queue)
q.dequeue() 
print(q.queue)
q.dequeue() 
print(q.queue)