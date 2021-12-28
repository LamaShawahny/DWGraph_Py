# This class represent an edge that connect two nodes in the graph

class EdgeData :
    def __init__(self, src, dest, weight, info, tag):
        self.src = src
        self.dest = dest
        self.weight = weight
        self.info = info
        self.tag = tag
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight


# src is the source node of the edge
# dest is the destination the of the edge
# info the info of the edge
# weight is the edges weight
# tag is the edges tag