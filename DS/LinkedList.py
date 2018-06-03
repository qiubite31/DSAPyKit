
class LinkedNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def __eq__(self, that):
        if self.val == that.val:
            return True

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

    def _search(self, tg_node):
        node = self.head
        pre_node = None
        while not tg_node == node:
            pre_node = node
            node = node.next
        else:
            return (pre_node, node)

    def insert(self, tg_node, new_item, loc='after'):
        if not self.head:
            return None

        pre_node, node = self._search(tg_node)
        new_node = self._append_item(new_item)
        if loc == 'after':
            new_node.next = node.next
            node.next = new_node
        elif loc == 'before':
            pre_node.next = new_node
            new_node.next = node
        else:
            return None

    def delete(self, tg_node):
        if not self.head:
            return None

        pre_node, node = self._search(tg_node)
        pre_node.next = node.next

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
singlylist.insert(LinkedNode(4), 7, loc='before')
singlylist.delete(LinkedNode(4))
print(singlylist)
