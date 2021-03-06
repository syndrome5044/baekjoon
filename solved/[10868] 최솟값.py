"""
problem tier : Gold 1 (solved.ac)
"""

import sys


class SegmentTree:
    def __init__(self, size, init=None):
        base = 1
        exp = 0
        while base < size:
            base *= 2
            exp += 1

        self.size = 2 ** exp
        self.init = init
        self.tree = [self.init for i in range(self.size * 2)]

    def update(self, index, value):
        return self._update(index, value, 1, 1, self.size)

    def _update(self, index, value, tree_index, section_left, section_right):
        if section_left == section_right:
            self.tree[tree_index] = value
        else:
            mid = (section_left + section_right) // 2
            if index <= mid:
                result = self._update(index, value, tree_index * 2, section_left, mid)
                self.tree[tree_index] = min(self.tree[tree_index], result)
            else:
                result = self._update(index, value, tree_index * 2 + 1, mid + 1, section_right)
                self.tree[tree_index] = min(self.tree[tree_index], result)
        return self.tree[tree_index]

    def query(self, start, end):
        return self._query(start, end, 1, 1, self.size)

    def _query(self, start, end, tree_index, section_left, section_right):
        if section_right < start or section_left > end:
            return self.init
        elif start <= section_left and section_right <= end:
            return self.tree[tree_index]
        else:
            mid = (section_left + section_right) // 2
            left_query = self._query(start, end, tree_index * 2, section_left, mid)
            right_query = self._query(start, end, tree_index * 2 + 1, mid + 1, section_right)
            min_value = min(left_query, right_query)
            return min_value


N, M = map(int, input().split())

tree = SegmentTree(size=N, init=2000000000)

for i in range(N):
    tree.update(i+1, int(sys.stdin.readline()))

for i in range(M):
    s, e = map(int, sys.stdin.readline().split())
    print(tree.query(s, e))
