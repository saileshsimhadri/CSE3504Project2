from Parser import Parser
from Graph import Graph
import numpy as np

class PageRank:

    def __init__(self, file, damp):
        p = Parser()
        self.graph, self.links = p.parse(file)
        size = len(self.graph.nodes)
        self.init_vec = np.array([[1/size for row in range(size)]])
        self.tran_matr = self.create_matrix()
        self.damp = damp
        self.dampen()

    def create_matrix(self):
        size = len(self.graph.nodes)
        matrix = np.zeros(shape=(size, size), dtype=np.float64)
        for node in self.graph:
            i = int(node.index) - 1
            deg = node.degree()
            for other_node in node:
                matrix[i][int(other_node.index) - 1] = 1/deg
        return matrix

    def dampen(self):
        self.tran_matr = self.damp * self.tran_matr + (1 - self.damp)/len(self.graph.nodes)

    def run(self, iterations):
        result = np.dot(self.init_vec, self.tran_matr)
        for x in range(60):
            result = np.dot(result, self.tran_matr)
            print(result)
        return result


