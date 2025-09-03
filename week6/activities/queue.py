class Queue:
    def __init__(self):
        self.list = []

    def enqueue(self, item):
        self.list.append(item)

    def is_empty(self):
        if not self.list:
            return True
        else:
            return False

    def dequeue(self):
        if self.is_empty():
            return True
        else:
            return self.list.pop(0)

    def peek(self):
        if self.is_empty():
            print("List is empty")
            return None
        else:
            return self.list[0]


new_queue = Queue()

new_queue.enqueue("apple")
new_queue.enqueue("banana")
new_queue.enqueue("pear")

new_queue.dequeue()

print(new_queue.peek())
print(new_queue.list)