############## Manual Stack ################
stack = [0]

stack.append(10)
stack.append(20)
stack.append(30)
stack.append(40)
 
print(stack)
print("(LIFO) Last-in First-out")
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())

stack = list()
for i in range(0, 100, 10):
	stack.append(i)
print(stack)
o = len(stack)

print(f"\n{stack.pop()}\n")
while stack:
	print(stack.pop())
print(stack)

############### Stack with Modules ################

import collections

print("with collections.deque()")
stack = collections.deque()
print(stack)
stack.append(10)
stack.append(20)
stack.append(30)
stack.append(40)
print(stack)

print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())

import queue

print("with queue.LifoQueue()")
stack = queue.LifoQueue()
stack.put(10)
stack.put(20)
stack.put(30)
stack.put(40)
print(stack)
print(stack.get())
print(stack.get())
print(stack.get())
print(stack.get())
#print(stack.get(timeout=1))