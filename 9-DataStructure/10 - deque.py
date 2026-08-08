# class Node :
#     def __init__(self,data):
#         self.data = data
#         self.next = None
#         self.prev = None

# class Doubly_Linked_List:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         new_node = Node(data)

#         if self.head is None:
#             self.head = new_node
#             return

#         current = self.head
#         while current.next is not None:
#             current = current.next

#         current.next = new_node
#         new_node.prev = current

from collections import deque

dq = deque([1,3,2,4,3,6,1,43,5,10])

# print(len(dq))

# dq.appendleft(0)

# dq.extend

# dq.rotate(4)

print(dq.index(1,0,4))