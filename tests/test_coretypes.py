import numpy as np
import networkx as nx

from simtypes.coretypes import Node
from simtypes.electric_elements_types.passive_elements import Resistor


class TestNode:
    first_node_instance = Node(node_id=1, name='one')
    second_node_instance = Node(node_id=2)

    def test_str(self):
        assert str(self.first_node_instance) == "Node 'one' (1)"
        assert str(self.second_node_instance) == "Node '2' (2)"

    def test_repr(self):
        assert (repr(self.first_node_instance) ==
                str(type(self.first_node_instance)) + "Node 'one' (1)")

    def test_immutability(self):
        hash_before = hash(self.first_node_instance)
        self.first_node_instance.name = 'two'
        hash_after = hash(self.first_node_instance)
        assert hash_before == hash_after


class TestGraph:
    graph = nx.DiGraph()
    nodes = [Node(1, 'one'),
             Node(2, 'two'),
             Node(3, 'three'),]
    edges = [Resistor(resistance=1, name='1-2', graph_edge_id=1,
                      begin_node=nodes[0], end_node=nodes[1]),
             Resistor(resistance=1, name='2-3', graph_edge_id=2,
                      begin_node=nodes[1], end_node=nodes[2]),
             Resistor(resistance=1, name='3-1', graph_edge_id=3,
                      begin_node=nodes[2], end_node=nodes[0]),]

    def test_nodes_adding_correctness(self):
        try:
            self.graph.add_nodes_from(self.nodes)
            assert True
        except TypeError:
            assert False

    def test_edges_adding_correctness(self):
        try:
            self.graph.add_edges_from(self.edges)
            assert True
        except TypeError:
            assert False

    def test_incidence_matrix(self):
        incidence_matrix = nx.linalg.incidence_matrix(self.graph, oriented=True).toarray()
        correct_incidence_matrix = np.array([[-1.0, 0.0, 1.0],
                                             [1.0, -1.0, 0.0],
                                             [0.0, 1.0, -1.0]])
        assert (incidence_matrix == correct_incidence_matrix).all()
