"""UnionFind.py
Author: BO WANG
Date: 09/18/2014
Union-find data structure to reduce complexity from O(mn) to O(mlogn)
"""

class UnionFind:
    def __init__(self):
        """create a empty Union-find structure"""
        self.parents = dict()
        self.numbers = dict()

    def __getitem__(self, item):
        """Find the root of the item"""
        # initialization
        if item not in self.parents:
            self.parents[item] = item
            self.numbers[item] = 1
            return item

        # find path and assign them the same root
        path = [item]
        root = self.parents[item]

        while root != path[-1]:
            path.append(root)
            root = self.parents[root]

        return root

    def union(self, u, v):
        """compare the roots of vertices u, v,
            if different, change the root of the subset that has less number"""
        r1 = self[u]
        r2 = self[v]

        if self.numbers[r1] > self.numbers[r2]:
            self.numbers[r1] += self.numbers[r2]
            self.parents[r2] = r1
        else:
            self.numbers[r2] += self.numbers[r1]
            self.parents[r1] = r2


