class Matrix:

    def __init__(self, height, width):
        self.m = []
        self.width = width
        self.height = height
        for i in range(0, height):
            self.m.append([0] * width)

    def __str__(self):
        return str(self.m)

    def __repr__(self):
        return self.__str__()

    def __iter__(self):
        for i in self.m:
            yield i

    def __getitem__(self, val):
        return self.m[val]

    def __mul__(self, other):
        if (self.width != other.height):
            raise Exception("Can't multiply")

        m = Matrix(self.height, other.width)

        for k in range(0, m.height):
            for l in range(0, m.width):
                temp = 0
                for i in range(0, self.width):
                    temp += self[k][i] * other[i][l]
                m[k][l] = temp
        return m
