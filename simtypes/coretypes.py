"""
Core types module consists of basic graph element: Node and Edge classes.
"""
from abc import ABC
from typing import Any


class Node:
    """
    Implements a graph node of the simulation model.
    It's a mutable type that can't be changed in runtime.
    """
    def __init__(self, node_id: int, name: str = ""):
        self.name = str(node_id) if not name else name
        self.__id = node_id

    def __str__(self):
        return f"Node '{self.name}' ({self.__id})"

    def __repr__(self):
        return str(type(self)) + f"Node '{self.name}' ({self.__id})"

    def __hash__(self):
        self._hash = hash(self.__id)
        return self._hash


class Edge(ABC):
    """
    An abstract graph edge class. It can be extended by child classes to
    implement an elementary part of a system.
    """
    def __init__(self, name: str, graph_edge_id: int,
                 begin_node: Node, end_node: Node):
        self.name = name
        self.begin_node = begin_node
        self.end_node = end_node
        self.graph_edge_id = graph_edge_id
        self.nodes = (self.begin_node, self.end_node)

    def __len__(self):
        return len(self.nodes)

    def __iter__(self):
        return iter(self.nodes)

    def get_branch_info(self):
        if type(self.begin_node) is not Node or type(self.end_node) is not Node:
            raise TypeError

        return (f"{type(self)}|{self.graph_edge_id}|"
                f"{self.begin_node.name} -> {self.end_node.name}")
