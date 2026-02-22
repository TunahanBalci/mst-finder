import sys

"""
Performs various checks and returns the number of vertices in the graph

Time complexity: O(n^2) 
"""
def get_length(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
        first_line = lines[0].strip()
        if (len (first_line.split()) < 2):
            raise Exception("Not a graph")
        
        x = 0
        for line in lines:
            for number in line.split():
                x += 1
                if not number.isdigit():
                    raise Exception("Invalid values in graph")
                
        if (x != len(lines) * len(lines)):
            raise Exception("Not a graph")
        
        return len(lines)
    
"""
Converts the graph from file in file_path to a 2D list and returns it

Time complexity: O(n^2)
"""
def get_graph(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
        graph = [[0 for column in range(len(lines))]
                 for row in range(len(lines))]
        for i in range(len(lines)):
            line = lines[i].strip()
            numbers = line.split()
            for j in range(len(numbers)):
                graph[i][j] = int(numbers[j])
        return graph

"""
Prim's algorithm implementation
"""
class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def print_mst(self, source):
        print("Edge     ---    Weight")
        for i in range(1, self.V):
            print(source[i], "-", i, "\t", self.graph[source[i]][i])

    def minimum_key(self, key, mst_sub_group):
        min = sys.maxsize

        for v in range(self.V):
            if key[v] < min and mst_sub_group[v] == False:
                min = key[v]
                min_index = v

        return min_index

    def prim(self):

        key = [sys.maxsize] * self.V
        
        source = [None] * self.V
        
        key[0] = 0
        
        mstSet = [False] * self.V

        source[0] = -1

        for cout in range(self.V):

            u = self.minimum_key(key, mstSet)
            mstSet[u] = True
            for v in range(self.V):

                if self.graph[u][v] > 0 and mstSet[v] == False \
                and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    source[v] = u

        self.print_mst(source)


if __name__ == '__main__':

    file = input("Enter the file path (default: udg.dat): ")

    if (file is None or file == "" or file == ''):
        file = "udg.dat"

    g = Graph(get_length(file))
    g.graph = get_graph(file)

    g.prim()