
class LinkedNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class SinglyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def _append_item(self, item):
        if isinstance(item, LinkedNode):
            return item
        else:
            return LinkedNode(item)

    def append(self, new_item):
        if not self.tail:
            self.head = self._append_item(new_item)
            self.tail = self.head
        else:
            self.tail.next = self._append_item(new_item)
            self.tail = self.tail.next

    def _append(self, new_node):
        if not self.head:
            self.head = self._append_item(new_node)
        else:
            node = self.head
            while node.next:
                node = node.next

            node.next = self._append_item(new_node)

    def __str__(self):
        items = []
        node = self.head
        while node is not None:
            items.append(node.val)
            node = node.next

        return str(items)


node = LinkedNode(3)
singlylist = SinglyLinkedList()
singlylist.append(node)
singlylist.append(LinkedNode(4))
singlylist.append(5)
print(singlylist)
