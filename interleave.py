from queue import Queue
def interLeaveQueue(q):
	if (q.qsize() % 2 != 0):
		print("Input even number of integers.")
	s = []
	halfSize = int(q.qsize() / 2)
	for i in range(halfSize):
		s.append(q.queue[0])
		q.get()
	while len(s) != 0:
		q.put(s[-1])
		s.pop()
	for i in range(halfSize):
		q.put(q.queue[0])
		q.get()
	for i in range(halfSize):
		s.append(q.queue[0])
		q.get()
	while len(s) != 0:
		q.put(s[-1])
		s.pop()
		q.put(q.queue[0])
		q.get()



queue = Queue()
queue.put(11)
queue.put(12)
queue.put(13)
queue.put(14)
queue.put(15)
queue.put(16)
queue.put(17)
queue.put(18)
queue.put(19)
queue.put(20)
interLeaveQueue(queue)
length = queue.qsize()
for i in range(length):
    print(queue.queue[0], end = " ")
    queue.get()


