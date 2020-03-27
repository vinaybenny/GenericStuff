# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 16:02:58 2020

@author: vinay.benny
"""
import numpy as np

class Node(object):
    def __init__(self, name, value, incoming=[], outgoing=[]):
        self.incoming_edges = [node for node in incoming]
        self.outgoing_edges = [node for node in outgoing]
        self.name = name
        self.value = value
        
class Graph(object):
    def __init__(self, nodes):
        self.nodes = dict()        
        for node in nodes:
            self.nodes.update({node.name : node})            
            
    def add_edge(self, node1, node2):
        self.nodes[node1.name].outgoing_edges.append(node2.name)
        self.nodes[node2.name].incoming_edges.append(node1.name)
        
    def remove_edge(self, node1, node2):
        self.nodes[node1.name].outgoing_edges.remove(node2.name)
        self.nodes[node2.name].incoming_edges.remove(node1.name)
        

class Heap(object):
    
    def __init__(self, array):
        nodes = []
        for idx, val in enumerate(array):
            nodes.append(Node(idx + 1, val))
         
        self.tree = Graph(nodes)    
            
        for node in nodes:                
            if 2*node.name <= len(array):
                self.tree.add_edge(node, self.tree.nodes[2*node.name])                
            if 1 + 2*node.name <= len(array):
                self.tree.add_edge(node, self.tree.nodes[1 + 2*node.name])
                
    def remove_node(self, node):
        for node_id in node.incoming_edges:
            self.tree.remove_edge(self.tree.nodes[node_id], node)
        self.tree.nodes.pop(node.name, None)
                
    def max_heapify(self, node):
        if len(node.outgoing_edges) == 0:
            return
        if len(node.outgoing_edges) == 1:
            left_node = self.tree.nodes[node.outgoing_edges[0]]  
            if node.value < left_node.value:
                node.value, self.tree.nodes[node.outgoing_edges[0]].value = self.tree.nodes[node.outgoing_edges[0]].value, node.value
                self.max_heapify(self.tree.nodes[node.outgoing_edges[0]])
            
        if len(node.outgoing_edges) == 2:
            left_node = self.tree.nodes[node.outgoing_edges[0]] 
            right_node = self.tree.nodes[node.outgoing_edges[1]]        
            if node.value < max(left_node.value, right_node.value):                
                if left_node.value >= right_node.value:
                    temp = node.value
                    node.value = left_node.value
                    self.tree.nodes[node.outgoing_edges[0]].value = temp
                    #node.value, self.tree.nodes[node.outgoing_edges[0]].value = self.tree.nodes[node.outgoing_edges[0]].value, node.value
                    self.max_heapify(self.tree.nodes[node.outgoing_edges[0]])
                else:
                    temp = node.value
                    node.value = right_node.value
                    self.tree.nodes[node.outgoing_edges[1]].value = temp
                    #node.value, self.tree.nodes[node.outgoing_edges[1]].value = self.tree.nodes[node.outgoing_edges[1]].value, node.value
                    self.max_heapify(self.tree.nodes[node.outgoing_edges[1]])
            
            
    def build_max_heap(self):
        for i in range(-1*int(len(self.tree.nodes)/2), 0):
            self.max_heapify(self.tree.nodes[-i])

        
    def heap_sort(self):
         self.build_max_heap()
         sorted_array = []
         
         while len(self.tree.nodes) > 0:
             # Swap the max element (i.e. teh root node with the last node)
             temp = self.tree.nodes[1].value
             self.tree.nodes[1].value = self.tree.nodes[len(self.tree.nodes)].value
             self.tree.nodes[len(self.tree.nodes)].value = temp
             sorted_array.append(temp)
             self.remove_node(self.tree.nodes[len(self.tree.nodes)])
             if len(self.tree.nodes) != 0:
                 self.max_heapify(self.tree.nodes[1]) 
         
         return sorted_array
         
         
        
        
        
if __name__ == "__main__":

    array = np.random.randint(100, size=(1,10))[0]
    print(array)
    y = Heap(array)          
    sorted_array = y.heap_sort()
    print(sorted_array)    
