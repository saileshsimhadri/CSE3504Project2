from Graph import Graph, Node, Edge

class Parser:

    def parse(self, file):
        nodes = {}
        edges = []
        links = {}
        with open(file) as f:
            # skip first lin
            next(f)
            for line in f:
                if "http" in line: # if it contains "http" then it is a node
                    items = line.split(" ")
                    index = items[0] # first element is index
                    address = items[1] # second element is link
                    nodes[index] = Node(index, address) # create node
                    links[index] = address
                else:
                    n1, n2 = line.strip("\n").split(" ") # otherwise it is an edge
                    n1 = nodes[n1]
                    n2 = nodes[n2]
                    e = Edge(n1, n2) # create edge with two nodes
                    n1.add_edge(e) 
                    edges.append(e)
        g = Graph(nodes, edges)
        print('degree', g['1'].degree())
        return g, links

