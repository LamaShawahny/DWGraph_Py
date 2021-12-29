from unittest import TestCase
from src.DWGraph import DWGraph
from src.NodeData import NodeData
from src.EdgeData import EdgeData
from copy import copy, deepcopy

class TestDWGraph(TestCase):
    def test_v_size(self):
        gg = DWGraph()
        gg.add_node(1)
        gg.add_node(2)
        gg.add_node(3)
        gg.add_node(4)
        gg.add_node(5)
        gg.add_node(6)
        gg.add_node(7)
        gg.add_node(8)
        x = gg.v_size()
        y = 8
        self.assertEqual(x, y)

    def test_get_all_v(self):
        gr = DWGraph()
        for n in range(7):
            gr.add_node(n)

        gr.add_edge(4, 1, 1)
        gr.add_edge(1, 0, 0.5)
        gr.add_edge(1, 2, 1.313)
        gr.add_edge(7, 2, 12)
        gr.add_edge(1, 7, 40)
        gr.add_edge(4, 5, 12)
        gr.add_edge(3, 4, 22)
        gr.add_edge(4, 3, 13)
        gr.add_edge(6, 5, 19)

        nodes = gr.get_all_v()

        assert len(nodes) == 6 + 1

        assert isinstance(nodes, dict)
        for i in range(6):
            assert i in nodes.keys()

    def test_e_size(self):
        g = DWGraph()
        for n in range(4):
            g.add_node(n)
        g.add_edge(1,2,3)
        g.add_edge(0,3,0)
        assert 2==g.e_size()

    def test_remove_node(self):
        gg = DWGraph()
        gg.add_node(1)
        gg.add_node(2)
        gg.add_node(3)
        gg.add_node(4)
        gg.add_node(5)
        gg.add_node(6)
        gg.add_node(7)
        gg.add_node(8)
        gg.remove_node(1)
        gg.remove_node(2)
        gg.remove_node(3)
        gg.add_node(9)
        x = gg.v_size()
        y = 6
        self.assertEqual(x, y)

    def test_all_in_edges_of_node(self):
        gr = DWGraph()
        for n in range(7):
            gr.add_node(n)

        gr.add_edge(0, 1, 1)
        gr.add_edge(1, 0, 112)
        gr.add_edge(1, 2, 1.3)
        gr.add_edge(2, 3, 1.1)
        gr.add_edge(1, 3, 10)
        gr.add_edge(2, 1, 10)
        gr.add_edge(4, 5, 12)
        gr.add_edge(3, 4, 22)
        gr.add_edge(6, 3, 18)

        edge_in = gr.all_in_edges_of_node(0)
        assert 2 not in edge_in.keys()

        edge_in = gr.all_in_edges_of_node(1)
        assert 0 not in edge_in.keys()

        edge_in = gr.all_in_edges_of_node(3)
        assert 1 in edge_in.keys()

    def test_all_out_edges_of_node(self):
        gr = DWGraph()

        for n in range(5):
            gr.add_node(n)

        gr.add_edge(0, 1, 1)
        gr.add_edge(1, 0, 17)
        gr.add_edge(2, 1, 10)
        gr.add_edge(2, 4, 1.15)

        edge_in = gr.all_out_edges_of_node(2)
        assert 1 in edge_in.keys()

        edge_in = gr.all_out_edges_of_node(1)
        assert 0 in edge_in.keys()

        assert isinstance(edge_in, dict) == True

    def test_get_mc(self):
        gr = DWGraph()

        gr.add_node(1)
        gr.add_node(2)
        gr.add_node(3)
        gr.add_node(4)
        gr.add_node(5)
        gr.add_node(6)
        gr.add_node(7)

        gr.remove_node(7)
        gr.remove_node(1)

        gr.add_node(1)
        gr.add_edge(1, 2, 1.3)
        gr.add_edge(2, 3, 1.1)
        gr.add_edge(1, 3, 10)
        gr.add_edge(4, 5, 12)
        gr.add_edge(3, 4, 22)
        gr.add_edge(4, 6, 3)
        gr.add_edge(6, 3, 18)
        gr.remove_edge(1,2)

        mc = gr.get_mc()
        gr.add_node(7)
        gr.add_node(8)
        assert gr.get_mc() == mc + 2
        gr.remove_node(8)
        assert gr.get_mc() == mc + 3

    def test_getNode(self):
        gr = DWGraph()
        gr.add_node(1)
        gr.add_node(2)
        gr.remove_node(1)

        k = gr.getNode(1)
        n =None
        self.assertEquals(k, n)

        gr.add_node(1)
        k = gr.getNode(1)
        n = None
        self.assertNotEqual(k, n)

    def test_getEdge(self):
        gr = DWGraph()
        gr.add_node(1)
        gr.add_node(2)

        gr.add_edge(1,2,3)

        k = gr.getEdge(1,2)
        n = None
        self.assertNotEquals(k, n)


        gr.remove_edge(1,2)
        k = gr.getEdge(1,2)
        n = None
        self.assertEqual(k, n)

    def test_add_edge(self):
        gr = DWGraph()
        for n in range(7):
            gr.add_node(n)
        gr.add_edge(0, 1, 1)
        assert gr.e_size() == 1

        gr.add_edge(1, 0, 1.1)
        assert gr.e_size() == 1+1

        gr.add_edge(1, 3, 10)
        gr.add_edge(4, 5, 12)
        gr.add_edge(3, 4, 22)
        gr.add_edge(4, 6, 3)
        gr.add_edge(6, 3, 18)
        assert not 14 in gr.all_in_edges_of_node(4)

    def test_add_node(self):
        gr = DWGraph()
        for n in range(8):
            gr.add_node(n)
        assert gr.v_size()==8
        gr.add_node(2)
        gr.add_node(1)
        gr.add_node(12)
        assert gr.v_size() == 8+1

    def test_remove_node(self):
     g= DWGraph()
     for n in range(4):
         g.add_node(n)
     g.remove_node(1)
     b = g.getNode(1)
     assert b is None


def test_remove_edge(self):
        gr = DWGraph()
        for n in range(7):
            gr.add_node(n)

        gr.add_edge(4, 1, 1)
        gr.add_edge(1, 4, 1.1)
        gr.add_edge(1, 2, 1.3)
        gr.add_edge(2, 3, 98.31)
        gr.add_edge(1, 3, 1.55)

        assert gr.e_size() == 5
        gr.remove_edge(1,3)
        gr.add_edge(2, 1, 1.55)
        gr.remove_edge(1, 2)
        assert gr.e_size() == 4
        gr.remove_edge(1, 2)
        assert gr.e_size() == 4
        #here we remove something not exist then no changes on e_size
        gr.remove_edge(1, 2)
        assert gr.e_size() == 4+0