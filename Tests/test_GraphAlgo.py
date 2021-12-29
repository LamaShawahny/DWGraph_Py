from unittest import TestCase
from src.DWGraph import DWGraph
from src.GraphAlgo import GraphAlgo
from src.NodeData import NodeData
from src.EdgeData import EdgeData
from copy import copy, deepcopy
class TestGraphAlgo(TestCase):
    def test_shortest_path(self):
        gg = DWGraph()
        gg.add_node(0)
        gg.add_node(1)
        gg.add_node(2)
        gg.add_node(3)
        gg.add_node(4)
        gg.add_node(5)
        gg.add_node(6)
        gg.add_node(7)
        gg.add_node(8)
        gg.add_node(9)
        gg.add_edge(1, 2, 10)
        gg.add_edge(2, 3, 9)
        gg.add_edge(5, 7, 2)
        gg.add_edge(2, 1, 3)
        gg.add_edge(3, 4, 2)
        gg.add_edge(4, 5, 9)
        gg.add_edge(1, 5, 90)
        graph3 = GraphAlgo(gg)
        self.assertEqual(graph3.shortest_path(1, 5), (30, [1, 2, 3, 4, 5]))
        self.assertEqual(graph3.shortest_path(2, 3), (9, [2, 3]))

    def test_centerPoint(self):
        gg = DWGraph()
        gg.add_node(0)
        gg.add_node(1)
        gg.add_node(2)
        gg.add_node(3)
        gg.add_node(4)
        gg.add_node(5)
        gg.add_node(6)
        gg.add_node(7)
        gg.add_node(8)
        gg.add_node(9)
        gg.add_edge(1, 2, 10)
        gg.add_edge(2, 3, 9)
        gg.add_edge(5, 7, 2)
        gg.add_edge(2, 1, 3)
        gg.add_edge(3, 4, 2)
        gg.add_edge(4, 5, 9)
        gg.add_edge(1, 5, 90)
        graph = GraphAlgo(gg)
