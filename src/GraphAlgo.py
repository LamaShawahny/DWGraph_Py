# Here is the Algorithms for our graph
from typing import List
import matplotlib.pyplot as plt
from queue import PriorityQueue
import math
from src.NodeData import NodeData
from src.EdgeData import EdgeData
from src.DWGraph import DWGraph
import queue
import json
class GraphAlgo:
    def __init__(self,graph):
        self._q = []
        self._DikstraQ = []
        self._color = []
        self._p = []
        self._d =[]
        self._pred = []
        self._dist = []
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
        edges = self._graph.get_all_edges()
        nodes = self._graph.get_all_v()
        json_file = {}
        jsonEdges = []
        jsonNodes = []

        for e in edges:
            parsed_edge = {'src': e.src.key, 'dest': e.dest.key, 'w': e.weight}
            jsonEdges.append(parsed_edge)

        for k in nodes.values():
            if k.getPos() is not None:
                pos = k.getPos()
                parsed_node = {'pos': pos, 'id': k.key}
            else:
                parsed_node = {'id': k.key}
            jsonNodes.append(parsed_node)

        json_file["Edges"] = jsonEdges
        json_file["Nodes"] = jsonNodes
        print(json_file)
        with open(file_name, 'x') as fp:
            json.dump(json_file, fp)
            return True

    def Dikstra(self, start: int):
        self._pred = []
        self._dist = []
        self._visited = []
        for i in range(self._graph.v_size()):
            self._dist.append(float('inf'))
            self._visited.append(False)
            self._pred.append(-1)
        self._dist[start] = 0
        dikstra1 = []
        for i in self._graph.get_all_v():
            dikstra1.append(self._graph.getNode(i.key))
        while len(dikstra1) > 1:
            u = self._graph.getNode(GraphAlgo.ExtractMin(self, dikstra1))
            dikstra1.remove(u)
            for edge in self._graph.all_out_edges_of_node(u.key).keys():
                e = self._graph.getEdge(u.key, edge.key)
                v = e.dest.key
                if self._visited[v] == False:
                    t = self._dist[u.key] + self._graph.getEdge(u.key, v).weight
                    if self._dist[v] > t:
                        self._dist[v] = t
                        self._pred[v] = u.key
            self._visited[u.key] = True

    def ExtractMin(self, list):
        index = -1
        min = float('inf')
        for i in range(len(list)):
            if self._dist[list[i].key] <= min:
                min = self._dist[list[i].key]
                index = list[i].key
        return index

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        if id1 == id2:
            l=[]
            l.append(self._graph.getNode(id1))
            return 0, l
        if self._graph.getNode(id1) is None or self._graph.getNode(id2) is None :
            return -1 ,[]
        self.Dikstra(id1)
        path=[]
        t = id2
        n = self._graph.getNode(t)
        path.append(n)
        while t != id1 :
            t =self._pred[t]
            path.append(self._graph.getNode(t))
        new_path = []
        for i in range(len(path)):
            new_path.append(path[i])
        return self._dist[id2] , new_path

    def centerPoint(self) -> (int, float):

        #is connected
        if GraphAlgo.isConnected(self):
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
        for n in self._graph.get_all_v().values():
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
            node = q[len(q)-1]
            del q[len(q)-1]
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

    def isConnected(self):
        nill = -1
        node = self._graph.getNode(0)
        if node is not None:
            d = GraphAlgo.BFS(self,node.key)
            for i in range(len(d)):
                if d[i] is nill:
                    return False
            g = GraphAlgo.revresed()
            node = g.getNode(0)
            d = GraphAlgo.BFS(self,node.key)
            for i in range(len(d)):
                if d[i] is nill:
                    return False
        return True

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        x=0
        ToGo = []
        path=[]
        path.append(node_lst[0])
        for i in range(len(node_lst)):
            ToGo.append(node_lst[i])
        while len(ToGo)>0:
            srcToDstPath = self.shortest_path(path[len(path)-1],ToGo[0])[1]
            for n in srcToDstPath:
                if n.key in ToGo:
                    if n.key in ToGo:
                        if len(srcToDstPath) != 1:
                            ToGo.remove(n.key)
                            path.append(n.key)
                        else:
                            ToGo.remove(n.key)

        return path

    def plot_graph(self) -> None:
        v = self._graph.get_all_v()
        e = self._graph.get_all_edges()
        for nd in v:
            nw = self._graph.getNode(nd)
            x = nw.getPos()[0]
            y = nw.getPos()[1]
            plt.plot(x, y, markersize=10, marker="o", color="green")
            plt.text(x, y, str(nd), color="black", fontsize=12)
            for edge in self._graph.all_out_edges_of_node(nd):
                pickNodeSrc = self._graph.getNode(nd)
                pickNodeDst = self._graph.getNode(edge.key)

                dstx = pickNodeDst.getPos()[0]
                dsty = pickNodeDst.getPos()[1]

                srcx = pickNodeSrc.getPos()[0]
                srcy = pickNodeSrc.getPos()[1]
                plt.annotate("", xy=(srcx, srcy), xytext=(dstx, dsty), arrowprops=dict(arrowstyle="<-"))
        plt.show()





