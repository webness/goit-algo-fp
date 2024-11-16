class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def merge_sort(self):
        if not self.head or not self.head.next:
            return

        self.head = self._merge_sort(self.head)

    def _merge_sort(self, head):
        if not head or not head.next:
            return head

        middle = self._get_middle(head)
        next_to_middle = middle.next
        middle.next = None

        left = self._merge_sort(head)
        right = self._merge_sort(next_to_middle)

        sorted_list = self._merge(left, right)
        return sorted_list

    def _get_middle(self, head):
        if not head:
            return head

        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def _merge(self, left, right):
        if not left:
            return right
        if not right:
            return left

        if left.value <= right.value:
            result = left
            result.next = self._merge(left.next, right)
        else:
            result = right
            result.next = self._merge(left, right.next)

        return result

    @staticmethod
    def merge_sorted_lists(li1, li2):
        dummy = Node(0)
        tail = dummy

        while li1 and li2:
            if li1.value <= li2.value:
                tail.next = li1
                li1 = li1.next
            else:
                tail.next = li2
                li2 = li2.next
            tail = tail.next

        # Add any remaining nodes
        if li1:
            tail.next = li1
        if li2:
            tail.next = li2

        return dummy.next


if __name__ == "__main__":
    ll = LinkedList()
    ll.append(4)
    ll.append(2)
    ll.append(5)
    ll.append(1)
    ll.append(3)

    print("Original List:")
    ll.print_list()

    ll.reverse()
    print("\nReversed List:")
    ll.print_list()

    ll.reverse()  # Re-reverse to get the original
    ll.merge_sort()
    print("\nSorted List:")
    ll.print_list()

    list1 = LinkedList()
    list1.append(1)
    list1.append(3)
    list1.append(5)

    list2 = LinkedList()
    list2.append(2)
    list2.append(4)
    list2.append(6)

    merged_head = LinkedList.merge_sorted_lists(list1.head, list2.head)

    print("\nMerged Sorted List:")
    current = merged_head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")
