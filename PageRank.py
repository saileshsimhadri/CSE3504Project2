from Parser import Parser
from Graph import Graph

class PageRank:

    def __init__(self, file):
        p = Parser()
        self.graph, self.links = p.parse(file)
        print(len(self.graph.nodes), len(self.graph.edges))
