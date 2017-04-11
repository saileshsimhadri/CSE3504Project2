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
            yield edge

    def add_edge(self, edge):
        self.edges[edge.other(self)] = edge

class Edge:

    def __init__(self, node1, node2):
        node1.add_edge(self)
        node2.add_edge(self)

    def other(self, node):
        if node == node1:
            return node2
        else:
            return node1



class Graph:

    def __init__(self, nodes, edges):
        self.nodes = {}
        self.edges = edges
        for node in nodes:
            self.nodes[node.value] = node

    def __getitem__(self, key):
       return self.nodes [key]

    def __iter__(self):
       for node in self.nodes.values():
           yield node
