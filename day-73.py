"""
This problem was asked by Google.

Given the head of a singly linked list, reverse it in-place.
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            temp = Node(value)
            temp.next = self.head
            self.head = temp

    def printList(self):
        curr = self.head
        while curr is not None:
            print(curr.value, end=' ')
            curr = curr.next
        print()

    def reverseList(self):
        prev = None
        curr = self.head
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev

myList = LinkedList()
myList.add(1)
myList.add(2)
myList.add(3)
myList.printList()
myList.reverseList()
myList.printList()