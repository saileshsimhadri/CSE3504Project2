from Parser import Parser
import math
from Graph import Graph
import numpy as np
import operator

class PageRank:

    def __init__(self, file):
        p = Parser()
        self.graph, self.links = p.parse(file)
        size = len(self.graph.nodes)
        self.init_vec = np.array([[1/size for row in range(size)]]).T # make a column vector with equal page ranks initially
        self.tran_matr = self.create_matrix() # create markov matrix

    def create_matrix(self):
        size = len(self.graph.nodes)
        matrix = np.zeros(shape=(size, size), dtype=np.float64)
        for node in self.graph:
            j = int(node.index) - 1
            deg = node.degree()
            if(deg == 0):
                for x in range(len(self.graph.nodes)):
                    matrix[x][j] = 1/len(self.graph.nodes) # if node has no links, then we start over with equal probabilites
            for other_node in node:
                i = int(other_node.index) - 1
                matrix[i][j] = 1/deg # if j links to i, then p(i,j)=1/deg(j)
        return matrix

    def dampen(self, damp):
        self.tran_matr = damp * self.tran_matr + (1 - damp)/len(self.graph.nodes) # return dampended matrix

    def epsilon(self, m1, m2): # calculates distance between two successive iterations to know when to stop
        diff = m1 - m2
        return math.sqrt(np.dot(diff, diff.T)[0][0])


    def run(self, damp):
        self.dampen(damp) # first dampen the matrix
        old_res = np.dot(self.tran_matr, self.init_vec) # perform one iteration
        new_res= np.dot(self.tran_matr, old_res) # perform another iteration
        while(self.epsilon(old_res, new_res) > .00000000001): # while we haven't converged, continue to peform iterations
            old_res = new_res
            new_res = np.dot(self.tran_matr, old_res)
        result = [(new_res[x][0], self.graph[str(x + 1)]) for x in range(len(self.graph.nodes))] # get node and probability pairs
        result.sort(key=operator.itemgetter(0), reverse=True) # sort to get page ranks
        return result


