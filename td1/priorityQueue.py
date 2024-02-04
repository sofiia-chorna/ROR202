class PriorityQueue:
    def __init__(self):
        self.heap = []
    
    def heapify(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        smallest = index

        # Find the index of the smallest element among the current node and its children
        if left_child_index < len(self.heap) and self.heap[left_child_index] < self.heap[smallest]:
            smallest = left_child_index

        if right_child_index < len(self.heap) and self.heap[right_child_index] < self.heap[smallest]:
            smallest = right_child_index

        # If the smallest element is not the current node, swap them and recursively heapify the affected subtree
        if smallest != index:
            # Swap
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]

            # Recursion
            self.heapify(smallest)

    def insert(self, element):
        self.heap.append(element)
        self.bubble_up(len(self.heap) - 1)
    
    def bubble_up(self, index):
        parent_index = (index - 1) // 2
        
        # Base case: stop bubbling up if elem is a root or its parent is smaller
        if index == 0 or self.heap[parent_index] <= self.heap[index]:
            return

        # Swap
        self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]

        # Recursion
        self.bubble_up(parent_index)

    def extract_min(self):
        if len(self.heap) == 0:
            return None
        
        min_element = self.heap[0]
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.heap.pop()
        self.heapify(0)

        return min_element
    
    def isEmpty(self):
        return len(self.heap) == 0