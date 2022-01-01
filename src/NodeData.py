# This class represent a  node in graph
class NodeData:
    def __init__(self, key, weight, info, tag , pos: tuple=None):
        self.key = key
        self.weight = weight
        self.info = info
        self.tag = tag
        self.pos = pos

    def __init__(self, key,pos):
        self.key = key
        self.pos=pos

    def __init__(self, key):
        self.key = key


    def getPos(self):
        return self.pos
# key is the key of the  node
# location is the location of the node
# info the info of the node
# weight is the node weight
# tag is the node tag