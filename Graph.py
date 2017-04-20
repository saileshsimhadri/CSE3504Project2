class Node:

    def __init__(self, index, value, *edges):
        self.index = index
        self.value = value
        self.edges = {}
        for edge in edges:
            self.add_edge(edge)

    def __getitem__(self, key):
        return self.edges[key]

    def __iter__(self):
        for edge in self.edges.values():
            yield edge.dest()

    def add_edge(self, edge):
        self.edges[edge.dest().index] = edge

    def degree(self):
        return len(self.edges)

class Edge:

    def __init__(self, node1, node2):
        self.origin = node1
        self.destination = node2

    def dest(self):
        return self.destination

class Graph:

    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges

    def __getitem__(self, key):
        return self.nodes[key]

    def __iter__(self):
       for node in self.nodes.values():
           yield node
