import sys

from graph import Graph
from utils import get_length, get_graph, validate_graph

if __name__ == '__main__':

    file = "udg.dat"

    g = Graph(get_length(file))
    g.graph = get_graph(file)
    validate_graph(g.graph)

    g.prim()