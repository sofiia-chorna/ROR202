class DisjointSet:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [0] * size

    def find(self, element):
        # Find the representative (root) of the set that contains the given element
        elemParent = self.parent[element]
        
        # It's not a root
        if elemParent != element:
            elemParent = self.find(elemParent)

        # Finish the recursion
        return elemParent

    def union(self, elem1, elem2):
        # Merge the sets containing elem1 and elem2
        root1 = self.find(elem1)
        root2 = self.find(elem2)

        rank1 = self.rank[root1]
        rank2 = self.rank[root2]
        
        if rank1 > rank2:
            self.parent[root2] = root1
        elif rank1 == rank2:
            self.parent[root1] = root2
            rank2 += 1
        else:
            self.parent[root1] = root2

    def print_hierarchy(self):
        forest = {}
        for i in range(len(self.parent)):
            root = self.find(i)
            if root not in forest:
                forest[root] = [i]
            else:
                forest[root].append(i)
        
        for root, nodes in forest.items():
            print(f"Root: {root}")
            print("  |--", end="")
            print(*nodes, sep=" -> ")


# ds = DisjointSet(5)

# ds.union(0, 1)
# ds.union(2, 3)
# ds.union(3, 0)
# # ds.union(0, 4)
# ds.print_hierarchy()

# print(ds.find(3))
