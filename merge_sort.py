class Solution:
    def middle(self,node):
        if node == None:
            return node
        slow = node
        fast = node
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow
    def sorted_merge(self,a, b):
        result = None
        if a == None:
            return b
        if b == None:
            return a
        if a.data <= b.data:
            result = a
            result.next = self.sorted_merge(a.next, b)
        else:
            result = b
            result.next = self.sorted_merge(a, b.next)
        return result
    def mergeSort(self,node):
        if node == None or node.next == None:
            return node
        middle_node = self.middle(node)
        nextmiddle = middle_node.next
        middle_node.next = None
        left = self.mergeSort(node)
        right = self.mergeSort(nextmiddle)
        sortedlist = self.sorted_merge(left, right)
        return sortedlist
        
        


import atexit
import io
import sys



# Node Class
class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node    
            return
        self.tail.next = new_node
        self.tail = new_node

# prints the elements of linked list starting with head
def printList(head):
    if head is None:
        print(' ')
        return
    curr_node = head
    while curr_node:
        print(curr_node.data,end=" ")
        curr_node=curr_node.next
    print(' ')


if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        n = int(input())
        p = LinkedList() # create a new linked list 'a'.
        nodes_p = list(map(int, input().strip().split()))
        for x in nodes_p:
            p.append(x)  # add to the end of the list

        printList(Solution().mergeSort(p.head))

