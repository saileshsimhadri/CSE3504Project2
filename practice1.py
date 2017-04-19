from PageRank import PageRank

def rank():
    pg = PageRank("hollins.dat")
    write(pg.run(.85), "output1.txt")
    write(pg.run(.95), "output2.txt")
    write(pg.run(.5), "output3.txt")

def write(result, file):
    with open(file, 'w') as f:
        for x in result:
            f.write(str(x[1].index) + " " + str(x[1].value) + "\n")
    f.close()

if __name__ == "__main__":
    rank()
