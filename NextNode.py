class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def removeConsecutiveSumTo0(node):

    while node:
        while node:
            sum = sum+node
            node = node.next
            if sum == 0:

    return node

node = Node(10)
node.next = Node(5)
node.next.next = Node(-3)
node.next.next.next = Node(-3)
node.next.next.next.next = Node(1)
node.next.next.next.next.next = Node(4)
node.next.next.next.next.next.next = Node(-4)
node = removeConsecutiveSumTo0(node)
while node:
  print node.value,
  node = node.next
# 10