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
        graph3 = GraphAlgo()
        graph3.init(gg)
        self.assertEqual(graph3.shortest_path(1, 5), (30, [1, 2, 3, 4, 5]))
        self.assertEqual(graph3.shortest_path(2, 3), (9, [2, 3]))

    def test_centerPoint(self):
        g = DWGraph()
        g.add_node(0)
        g.add_node(1)
        g.add_node(2)
        g.add_node(3)
        g.add_node(4)
        g.add_edge(0, 1, 1)
        g.add_edge(1, 2, 1)
        g.add_edge(2, 1, 1)
        g.add_edge(1, 0, 1)
        g.add_edge(2, 3, 1)
        g.add_edge(3, 2, 1)
        g.add_edge(3, 4, 1)
        g.add_edge(4, 3, 1)

        g_algo = GraphAlgo()
        g_algo.init(g)
        self.assertEqual(g_algo.centerPoint().key, 2)

    def test_save_and_load_from_json(self):
        g = DWGraph()
        g.add_node(0, (0, 1, 2))
        g.add_node(1, (3, 4, 5))
        g.add_node(2, (6, 7, 8))
        g.add_node(3, (7, 6, 5))
        for i in range(3):
            g.add_edge(i, i + 1, i + 2)
        ga_original = GraphAlgo()
        ga_original.init(g)
        ga_original.save_to_json("j1")
        ga_loaded = GraphAlgo()
        returned_bool = ga_loaded.load_from_json("j1")
        self.assertTrue(returned_bool)
        ga_original.get_graph().getNode(0).pos = (0, 1.1, 2)
        ga_original.get_graph().getNode(0).pos = (0, 1, 2)
        ga_original.get_graph().remove_edge(0, 1)

    def test_TSP(self):
        list =[]
        g = DWGraph()
        for i in range(4):
            g.add_node(i)
            list.append(i)
        g.add_edge(0,1,10)
        g.add_edge(1, 0, 10)
        g.add_edge(0,3,20)
        g.add_edge(3,0,20)
        g.add_edge(0, 2, 20)
        g.add_edge(3, 0, 20)
        g.add_edge(0, 2, 15)
        g.add_edge(2, 0, 15)
        g.add_edge(1, 3, 25)
        g.add_edge(3, 1, 25)
        g.add_edge(3, 2, 30)
        g.add_edge(2, 3, 30)
        g.add_edge(1, 2, 35)
        g.add_edge(2, 1, 35)

        g_algo = GraphAlgo()
        g_algo.init(g)
        self.assertEqual(g_algo.TSP(list), [0,1,2,3])


