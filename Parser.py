class Parser:

    def parse(self, file):
        nodes = {}
        edges = []
        links = {}
        with open(file) as f:
            # skip first lin
            next(f)
            for line in f:
                if "http" in line:
                    index, address = line.split(" ")
                    nodes[index] = Node(index, value)
                    links[index] = address
                else:
                    n1, n2 = line.split(" ")
                    n1 = nodes[n1]
                    n2 = nodes[n2]
                    e = Edge(n1, n2)
                    n1.add_edge(e)
                    n2.add_edge(e)
        g = Graph(nodes, edges)
        return g, links

