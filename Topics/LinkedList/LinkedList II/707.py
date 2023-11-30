class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0
        
    def get(self, index: int) -> int:
        if index > self.size or index < 0:
            return -1
        curr = self.head
        n = 0
        while curr:
            if n == index:
                return curr.val
            curr = curr.next
            n += 1
        return -1


    def addAtHead(self, val: int) -> None:
       self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)
        

    def addAtIndex(self, index: int, val: int) -> None:

        if index > self.size:
            return
         
        newNode = ListNode(val)
        curr = self.head

        if index == 0:
            newNode.next = curr
            self.head = newNode

        else:
            n = 0
            prev = None

            while curr:
                if n == index :
                    break
                else:
                    prev = curr
                    curr = curr.next
                n += 1

            newNode.next = curr
            prev.next = newNode 

            

        self.size += 1

    # # to print
        curr = self.head
        while curr:
            print(curr.val)
            curr = curr.next
        print("Finish Output from append")
    


    def deleteAtIndex(self, index: int) -> None:

        if index >= self.size or index < 0:
            return 
        if index == 0:
            self.head = self.head.next

        else:
            prev = None
            curr = self.head
            n = 0
            while curr:
                if n == index :
                    prev.next = curr.next
                    break
                prev = curr
                curr = curr.next
                n += 1

        self.size -= 1







        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# obj.addAtHead(1)
# obj.addAtHead(2)
# obj.addAtHead(3)
# obj.addAtHead(4)
# obj.addAtHead(5)
# obj.addAtHead(6)
# obj.addAtHead(7)


# print(obj.get(5))
# print(obj.get(0))