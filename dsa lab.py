#FOR LINEAR QUEUES
class LinearQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.capacity

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full. Cannot enqueue element.")
        else:
            self.queue.append(item)
            print(f"Enqueued: {item}")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue element.")
            return None
        else:
            item = self.queue.pop(0)
            print(f"Dequeued: {item}")
            return item

    def display(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print("Queue:", self.queue)


# Test the linear queue implementation
queue = LinearQueue(5)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.display()
queue.dequeue()
queue.display()
queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6)
queue.display()


#FOR CIRCULAR QUEUES
class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full. Cannot enqueue element.")
            return
        elif self.is_empty():
            self.front = 0

        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
        print(f"Enqueued: {item}")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue element.")
            return

        item = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity

        print(f"Dequeued: {item}")
        return item

    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return

        current = self.front
        while current != self.rear:
            print(self.queue[current], end=" ")
            current = (current + 1) % self.capacity
        print(self.queue[self.rear])


# Test the circular queue implementation
cq = CircularQueue(5)
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
cq.display()
cq.dequeue()
cq.display()

#FOR QUEUES USING STACK
class QueueUsingStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        self.stack1.append(item)

    def dequeue(self):
        if not self.stack2:
            if not self.stack1:
                print("Queue is empty. Cannot dequeue element.")
                return None
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def display(self):
        if not self.stack2:
            if not self.stack1:
                print("Queue is empty")
                return
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        print(self.stack2)


# Test the queue using stacks implementation
qs = QueueUsingStacks()
qs.enqueue(1)
qs.enqueue(2)
qs.enqueue(3)
qs.display()
qs.dequeue()
qs.display()


