# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution3:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = ListNode(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = ListNode(data)

        if not self.head:
            self.head = new_node
            return  # ✔ return only here

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.val, end=" -> ")
            temp = temp.next
        print("NULL")

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current_node = head

        while current_node:
            new_node = current_node.next
            current_node.next = prev
            prev = current_node
            current_node = new_node

        return prev


ll = Solution3()

ll.insert_at_beginning(3)
ll.insert_at_beginning(2)
ll.insert_at_beginning(1)

ll.insert_at_end(4)
ll.insert_at_end(5)

ll.display()

ll.head = ll.reverseList(ll.head)

ll.display()
