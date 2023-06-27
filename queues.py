queue = list()

queue.append(23)
queue.append(4)
queue.append(8)
queue.append(75)
queue.append(36)
queue.append(55)

print(queue) # Expected: [23, 4, 8, 75, 36, 55]

queue.pop(3)
queue.pop(0)

print(queue) # Expected: [4, 8, 36, 55]