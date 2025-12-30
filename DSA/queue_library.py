from collections import deque

queue = deque()
queue.append(10)
queue.append(20)
queue.append(30)
queue.append(40)

print("Queue:", queue)

removed = queue.popleft()
print("Removed:", removed)

print("Front element:", queue[0])

print("Queue after dequeue:", queue)
