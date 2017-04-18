from PageRank import PageRank

def rank():
    pg = PageRank("hollins.dat", .85)
    print(pg.run(100))

if __name__ == "__main__":
    rank()
