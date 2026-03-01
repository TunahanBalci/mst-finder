"""
Performs various checks and returns the number of vertices in the graph

Time complexity: O(n^2) 
"""
def get_length(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

        # Filter out empty lines
        lines = [line for line in lines if line.strip()]

        if len(lines) == 0:
            raise Exception("Empty file")

        first_line = lines[0].strip()
        if (len(first_line.split()) < 2):
            raise Exception("Not a graph")
        
        n = len(lines)
        for line in lines:
            values = line.split()
            if len(values) != n:
                raise Exception("Not a square matrix: row has " + str(len(values)) + " values, expected " + str(n))
            for number in values:
                if not number.isdigit():
                    raise Exception("Invalid values in graph: '" + number + "' is not a non-negative integer")
                
        return n

"""
Validates that the adjacency matrix:
- when i = j, matrix[i][j] = 0
- len(matrix[i]) = len(matrix[j]), always

Time complexity: O(n^2)
"""
def validate_graph(graph):
    n = len(graph)
    for i in range(n):
        if graph[i][i] != 0:
            raise Exception("Invalid graph: diagonal entry [" + str(i) + "][" + str(i) + "] is " + str(graph[i][i]) + ", expected 0")
    for i in range(n):
        for j in range(i + 1, n):
            if graph[i][j] != graph[j][i]:
                raise Exception("Invalid Graph - Non symmetric matrix:" + str(i) + "][" + str(j) + "] (" + str(graph[i][j]) + " != " + str(graph[j][i]) + ")")

"""
Converts the graph from file in file_path to a 2D list

Time complexity: O(n^2)
"""
def get_graph(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
        lines = [line for line in lines if line.strip()]
        graph = [[0 for column in range(len(lines))]
                 for row in range(len(lines))]
        for i in range(len(lines)):
            line = lines[i].strip()
            numbers = line.split()
            for j in range(len(numbers)):
                graph[i][j] = int(numbers[j])
        return graph