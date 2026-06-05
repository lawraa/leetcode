class Node: 
    def __init__(self, key, val, next = None, prev = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next 


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = Node(0,0) # least recently used
        self.right = Node(0,0) # most recently used
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node: Node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node
    
    def insert(self, node: Node):
        prev_node = self.right.prev
        next_node = self.right

        prev_node.next = node
        node.prev = prev_node

        node.next = next_node
        next_node.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]

        self.remove(node)
        self.insert(node)
        
        return node.val
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            old_node = self.cache[key]
            self.remove(old_node)
        
        new_node = Node(key, value)
        self.cache[key] = new_node
        self.insert(new_node)
        
        if len(self.cache) > self.capacity:
            lru_node = self.left.next
            self.remove(lru_node)
            del self.cache[lru_node.key]

# Time complexity: O(1) for both get and put
# Space complexity: O(capacity)