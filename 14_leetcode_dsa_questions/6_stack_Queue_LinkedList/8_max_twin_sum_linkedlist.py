from typing import Optional


# -------------------------
# Node definition
# -------------------------
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# -------------------------
# Linked List class
# -------------------------
class Solution4:
    def __init__(self):
        self.head = None

    # Insert at end
    def insert_at_end(self, val):
        new_node = ListNode(val)

        if not self.head:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # Display linked list
    def display(self):
        temp = self.head
        while temp:
            print(temp.val, end=" -> ")
            temp = temp.next
        print("NULL")

    # -------------------------
    # Maximum Twin Sum (LC 2130)
    # -------------------------
    def pairSum(self, head: Optional[ListNode]) -> int:
        if not self.head:
            return 0

        # 1️⃣ Find middle of linked list
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2️⃣ Reverse second half
        prev = None
        curr = slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # 3️⃣ Compute maximum twin sum
        max_sum = 0
        first = self.head
        second = prev

        while second:
            max_sum = max(max_sum, first.val + second.val)
            first = first.next
            second = second.next

        return max_sum


# -------------------------
# Driver Code
# -------------------------
ll = Solution4()

# Insert elements
ll.insert_at_end(2)
ll.insert_at_end(5)
ll.insert_at_end(1)
ll.insert_at_end(7)

# Display linked list
print("Linked List:")
ll.display()

# Perform Maximum Twin Sum
result = ll.pairSum(ll.head)

print("Maximum Twin Sum:", result)
