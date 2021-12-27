# This class represent a  node in graph
class NodeData:
    def __init__(self, key, location, weight, info, tag):
        self.key = key
        self.location = location
        self.weight = weight
        self.info = info
        self.tag = tag

    def __init__(self, key):
        self.key = key
# key is the key of the  node
# location is the location of the node
# info the info of the node
# weight is the node weight
# tag is the node tag
