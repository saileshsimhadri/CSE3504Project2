from Parser import Parser
from Graph import Graph
import numpy as np
import operator

class PageRank:

    def __init__(self, file):
        p = Parser()
        self.graph, self.links = p.parse(file)
        size = len(self.graph.nodes)
        self.init_vec = np.array([[1/size for row in range(size)]]).T
        self.tran_matr = self.create_matrix()
        print(self.tran_matr)

    def create_matrix(self):
        size = len(self.graph.nodes)
        matrix = np.zeros(shape=(size, size), dtype=np.float64)
        for node in self.graph:
            j = int(node.index) - 1
            deg = node.degree()
            for other_node in node:
                i = int(other_node.index) - 1
                matrix[i][j] = 1/deg
        return matrix

    def dampen(self, damp):
        self.tran_matr = damp * self.tran_matr + (1 - damp)/len(self.graph.nodes)

    def epsilon(self, m1, m2):
        return max(abs(m1[x][0] - m2[x][0]) for x in range(len(self.graph.nodes)))


    def run(self, damp):
        self.dampen(damp)
        old_res = np.dot(self.tran_matr, self.init_vec)
        new_res= np.dot(self.tran_matr, old_res)
        while(self.epsilon(old_res, new_res) > .00001):
            old_res = new_res
            new_res = np.dot(self.tran_matr, old_res)
            print(self.epsilon(old_res, new_res))
        result = [(new_res[x][0], self.graph[str(x + 1)]) for x in range(len(self.graph.nodes))]
        result.sort(key=operator.itemgetter(0), reverse=True)
        return result


