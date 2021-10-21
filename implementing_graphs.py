class Graph:
    def __init__(self, V, E):
        self.V = set(V)
        self.E = set(E)
        

if __name__ == '__main__':
    G = Graph([1,2,3], {(1,4), (9,6)})