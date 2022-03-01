
class Node():
    def __init__(self,val) :
        self.val=val
        self.next=None
        
def reverseList(self, temp):  
        current = temp;  
        prevNode = None;  
        nextNode = None;  
          
        while(current != None):  
            nextNode = current.next;  
            current.next = prevNode;  
            prevNode = current;  
            current = nextNode;  
        return prevNode;      
def getSize(self, head):
    count = 0
    curr_node = head
    while curr_node:
        count +=1
        curr_node = curr_node.next
    return count   
def isPalindrome(self, head):  
    current = head;  
    flag = True;  
    s = self.getSize(head)
    mid = (s//2) if(s%2 == 0) else ((s+1)//2);  
    for i in range(1, mid):  
        current = current.next;   
    revHead = self.reverseList(current.next);  
    while(head != None and revHead != None):  
        if(head.data != revHead.data):  
            flag = False;  
            break;  
            
        head = head.next;  
        revHead = revHead.next  
    return flag