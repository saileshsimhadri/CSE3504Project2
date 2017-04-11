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
            yield edge.other(self)

    def add_edge(self, edge):
        self.edges[edge.other(self).index] = edge

class Edge:

    def __init__(self, node1, node2):
        self.node1 = node1
        self.node2 = node2
        node1.add_edge(self)
        node2.add_edge(self)

    def other(self, node):
        if node == self.node1:
            return self.node2
        else:
            return self.node1



class Graph:

    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges

    def __getitem__(self, key):
        print(self.nodes)
        return self.nodes[key]

    def __iter__(self):
       for node in self.nodes.values():
           yield node
