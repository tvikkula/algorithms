# A single list element:
class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


# The list itself:
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head


    # Append an element to the end of list:
    def append(self, new_element):
        current = self.head
        if self.head:
            # iterate over the linked list until
            # you find the last element (next is null):
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element


    # Get the element at a position in the list:
    def get_position(self, position):
        if position < 1:
            return None
        current = self.head
        for i in range(1, position):
            if current.next:
                current = current.next
            else:
                return None
        return current


    # Insert element at a given position:
    def insert(self, new_element, position):
        if position < 1:
            return
        if position == 1:
            new_element.next = self.head
            self.head = new_element
            return
        before = self.get_position(position - 1)
        new_element.next = before.next
        before.next = new_element


    # Delete an element with a specific value:
    def delete(self, position):
        prev = self.get_position(position - 1)
        if prev == None and self.head != None:
            prev = self.head
            # In first element, remove it:
            self.head = prev.next
            return prev
        else:
            return
        current = prev.next
        prev.next = current.next
        return current
