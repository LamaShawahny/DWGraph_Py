# This graph represnts the graph
from src.NodeData import NodeData
from  src.EdgeData import EdgeData
class DWGraph() :
   def __init__(self):
         self._nodes = {}  # this Dictionary contains our graph nodes
         self._edges = {}  # this Dictionary contains our graph edges
         self._MC = 0

   def v_size(self):
      return len(self._nodes)

   def e_size(self):
      return len(self._edges)

   def get_all_v(self):
       return self._nodes.keys()

   def get_all_edges(self):
       return self._edges.values()# edges-> edge data-> (id1 is dest) rfeturn dic of the sources

   def all_in_edges_of_node(self, id1: int):
       in_edges = {}
       for e in self._edges.keys():
           if self._edges[e].dest.key == id1:
               in_edges[self._edges[e].src] = self._edges[e].weight
       return in_edges

   def all_out_edges_of_node(self, id1: int):
       out_edges = {}
       for e in self._edges.keys():
           if self._edges[e].src.key == id1:
               out_edges[self._edges[e].dest] =self._edges[e].weight
       return out_edges

   def get_mc(self):
       return self._MC

   def getEdge(self, src: int, dest: int ):
       s = str(src) + "," + str(dest)
       if self._edges.__contains__(s):
           return self._edges.get(s)
       return None

   def getNode (self, key:int):
       if self._nodes.__contains__(key):
           return self._nodes.get(key)
       else :
           return None

   def add_edge(self, id1: int, id2: int, weight: float):
       if id1 == id2:
           return
       source = self._nodes.get(id1)
       dest = self._nodes.get(id2)

       if source is None or dest is None:
           return

       NewEdge = EdgeData(source,dest,weight)
       EdgeStr = str(id1) + "," + str(id2)

       self._edges[EdgeStr]=NewEdge
       self._MC = self._MC +1
       return True

   def add_node(self, node_id: int, pos: tuple = None):
       newNode = NodeData(node_id)
       if newNode not in self._nodes:
           self._nodes[node_id]=newNode
           self._MC = self._MC + 1
           return True



   def remove_node(self, node_id: int):
       if self._nodes.__contains__(node_id) is True:
           newNode= self._nodes.get(node_id)
       else: newNode= None
       if self._nodes.__contains__(node_id):
           del self._nodes[node_id]
           self._MC= self._MC+1
           list = self._edges.values()
           for edge in list :
               if edge.src is node_id or edge.dest is node_id:
                   EdgeStr = str(edge.src) + "," + str(edge.dest)
                   del self._edges[EdgeStr]
                   self._MC = self._MC + 1
           return True
       return

   def remove_edge(self, node_id1: int, node_id2: int):
        EdgeStr = str(node_id1) + "," + str(node_id2)
        if self._edges.__contains__(EdgeStr):
           del self._edges[EdgeStr]
           self._MC=self._MC+1
           return True
        return








