class Queue(object):
    def __init__(self):
        self.queue = []

    def push(self, item):
        self.queue.append(item)

    def pop(self):
        self.queue.pop(0)

    def __str__(self):
        return 'Exis<-' + str(self.queue) + ' <-Enter'


queue = Queue()
print(queue)
queue.push(2)
print(queue)
queue.push(3)
queue.pop()
print(queue)
queue.push(4)
print(queue)
queue.push(5)
print(queue)