from Queue import Queue

queue = Queue(4)
queue.enqueue(2)
queue.enqueue(1)
print('before dequeue:')
queue.print_queue()
queue.dequeue()
print('after dequeue:')
queue.print_queue()