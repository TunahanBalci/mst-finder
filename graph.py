import sys

"""
Prim's algorithm implementation
and graph class
"""
class Graph():
    def __init__(self, _vertices):
        self.vertices = _vertices
        self.graph = [[0 for column in range(_vertices)]
                      for row in range(_vertices)]

    def print_mst(self, source):
        total_weight = 0
        for i in range(1, self.vertices):
            total_weight += self.graph[source[i]][i]

            # self.graph[source[i]][i] => weighted edge

        print("Total weight of MST: ", total_weight)

    def save_mst(self, source, file_path="mst.dat"):
        mst = []

        for _ in range(self.vertices):
            mst.append([0] * self.vertices)

        for i in range(1, self.vertices):
            weight = self.graph[source[i]][i]
            mst[source[i]][i] = weight
            mst[i][source[i]] = weight
        with open(file_path, 'w') as f:
            for row in mst:
                f.write(' '.join(str(x) for x in row) + '\n')

    def minimum_key(self, key, mst_sub_group):
        min = sys.maxsize

        for v in range(self.vertices):
            if key[v] < min and mst_sub_group[v] == False:
                min = key[v]
                min_index = v

        return min_index

    def prim(self):

        key = [sys.maxsize] * self.vertices
        source = [None] * self.vertices
        key[0] = 0
        mstSet = [False] * self.vertices
        source[0] = -1

        for cout in range(self.vertices):

            u = self.minimum_key(key, mstSet)
            mstSet[u] = True
            for v in range(self.vertices):

                if self.graph[u][v] > 0 and mstSet[v] == False \
                and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    source[v] = u

        self.print_mst(source)
        self.save_mst(source)

