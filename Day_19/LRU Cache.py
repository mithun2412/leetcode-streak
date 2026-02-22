class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # hashmap

        # Dummy head & tail
        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head


    # Remove a node from DLL
    def remove(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node


    # Insert node right after head (most recent)
    def insert(self, node):
        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]

        # Move to front (recently used)
        self.remove(node)
        self.insert(node)

        return node.value


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Remove old node
            self.remove(self.cache[key])

        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)

        # Remove LRU if capacity exceeded
        if len(self.cache) > self.capacity:
            lru = self.tail.prev
            self.remove(lru)
            del self.cache[lru.key]