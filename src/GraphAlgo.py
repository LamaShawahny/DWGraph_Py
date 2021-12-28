# Here is the Algorithms for our graph
from typing import List
import math
from NodeData import NodeData
from EdgeData import EdgeData
from DWGraph import DWGraph
import queue
import json
class GraphAlgo:
    def __init__(self,graph):
        self._q = []
        self._DikstraQ = []
        self._color=[]
        self._p= []
        self._d =[]
        self._pred =[]
        self._dist =[]
        self._visited=[]
        self._nill = -1
        self._graph =graph


    def get_graph(self):
        return self._graph

    def load_from_json(self, file_name: str) -> bool:
        with open(file_name, 'r') as f:
            data = json.loads(f.read())
            nodes = data["Nodes"]
            for v in nodes:
                self._graph.add_node(node_id=v["id"], pos=v["pos"])
            edges = data["Edges"]
            for e in edges:
                self._graph.add_edge(id1=e["src"], id2=["dest"], weight=data["w"])

    def save_to_json(self, file_name: str) -> bool:
        data_nodes=[]
        for n in self._graph.get_all_v:
            n_dict = {}
            n_dict["pos"] = n.location
            n_dict["id"] = n.key
            data_nodes.append(n_dict)
        data_edges = []
        for e in self._graph.get_all_edges:
            e_dict ={}
            e_dict["src"] = e.src
            e_dict["dest"] = e.dest
            e_dict["w"] = e.weight
            data_edges.append(e_dict)
        with open(file_name, 'w') as outfile:
            json.dump(data_edges, outfile)
            json.dump(data_nodes, outfile)

    def Dikstra(self, start: int):
        for i in range(self._graph.v_size()):
            self._pred.append(self._nill)
            self._dist.append(float('inf'))
            self._visited.append( False)
        print(len(self._dist))
        self._dist[start] = 0

        for n in self._graph.get_all_v():
            self._DikstraQ.append(n)

        while len(self._DikstraQ) > 0:
            u = self._graph.getNode(GraphAlgo.ExtractMin(self,self._DikstraQ))
            if self._graph.getNode(GraphAlgo.ExtractMin(self,self._DikstraQ)) is not None:
                del self._DikstraQ[self._graph.getNode(GraphAlgo.ExtractMin(self,self._DikstraQ)).key]
            for e in self._graph.get_all_edges():
                v = e.dest
                print(len(self._visited))
                if self._visited[v.key]== False:
                    if self._graph.getEdge(u.key,v) is not None:
                        t = self._dist[u.key] + self._graph.getEdge(u.key,v).weight
                        if not self._dist[v] > t:
                            self._dist[v] = t
                            self._pred[v] = u.key
        self._visited[u.key]=True

    def ExtractMin(self,list):
        index= -1
        min = float('inf')
        for i in range(len(list)-1):
            if self._dist[list[i]] <= min:
                min = self._dist[list[i]]
                index = list[i]
        return index

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        if id1 == id2:
            return -1, []
        if self._graph.getNode(id1) is None or self._graph.getNode(id2) is None :
            return -1 ,[]
        GraphAlgo.Dikstra(self,id1)
        path=[]
        t = id2
        n = self._graph.getNode(t)
        path.append(n)
        while t is not id1 :
            t =self._pred[t]
            path.append(self._graph.getNode(t))
        new_path = []
        for i in range(len(path)):
            new_path.append(path[i])
        return self._dist[id2] , new_path

    def centerPoint(self) -> (int, float):

        #is connected
        if GraphAlgo.isConnectes() is True:
            n = self._graph.v_size()
            nVert =n
            leavs = []
            degrees=[]
            levels =[]
            for i in range[n]:
                crt=0
                for e in self._graph.get_all_edges():
                    crt= crt +1

                degrees[i]=crt
                if degrees[i] == 1:
                    leavs.append(i)
            maxLevel=0
            while(nVert>2):
                leaf= leavs.remove(len(leavs)-1)
                degrees[leaf]=0
                for k in self._graph.all_in_edges_of_node(leaf):
                    v= k.dest
                    degrees[v]=degrees[v]-1
                    self._graph.remove_edge(v,leaf)
                    nVert=nVert-1
                    if degrees[v] == 1:
                        leavs.append(v)
                        levels[v]=levels[leaf]+1
                        maxLevel= max(maxLevel,levels[v])
            centers =[]
            for i in range[n]:
                if levels[i] is maxLevel:
                    centers.append(i)
            numCenters = len(centers)
            if numCenters == 2:
                radius =maxLevel+1
                diameter = 2*radius-1
            else:
                radius =maxLevel
                diameter = 2*radius
            return self._graph.getNode(centers[0])
        else:
            return None

    def BFS(self, startnode):
        color = {}
        d = {}
        p = {}
        nill = -1
        for n in self._graph.get_all_v:
            color[n.key] = "white"
            d[n.key] = nill
            p[n.key] = nill
        color[startnode] = "gray"
        d[startnode] = 0
        p[startnode] = None
        q = []
        n = self._graph.getNode(startnode)
        q.append(n)
        while len(q) > 0:
            node = q.remove(len(q) - 1)
            for edge in self._graph.all_out_edges_of_node(node.key):
                i = self._graph.getNode(edge)
                if i is not None:
                    if color[i.key] == "white":
                        color[i.key] = "gray"
                        d[i.key] = d[node.key] + 1
                        p[i.key] = node
                        q.append(i)
        color[node.key] = "black"
        return d

    def revresed(self):
        gra = DWGraph()
        for n in self._graph.get_all_v():
            gra.add_node(n.key)
        for e in self._graph.get_all_edges:
            gra.add_edge(e.dest, e.src, e.weight)
        return gra

    def isConnectes(self):
        nill = -1
        node = self._graph.getNode(0)
        if node is not None:
            d = DWGraph.BFS(node.key)
            for i in range(len(d)):
                if d[i] is nill:
                    return False
            g = DWGraph.revresed()
            node = g.getNode(0)
            d = DWGraph.BFS(node.key)
            for i in range(len(d)):
                if d[i] is nill:
                    return False

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        x=0
        ToGo = set()
        path=[]
        path.append(node_lst[0])
        for i in range(len(node_lst)):
            ToGo.add(node_lst[i].key)
        while len(ToGo)>0:
            srcToDstPath = GraphAlgo.shortest_path(path[len(path)-1],ToGo[x])
            x = x+1
            for n in self._graph.get_all_v:
                ToGo.remove(n.key)
                path.append(n)

        return path







