# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 11:16:56 2020

@author: vinay.benny
"""
class BinaryNode(object):
    
    def __init__(self, value=None, left=None, right=None, parent=None):
        self._key = value
        self._left = left
        self._right = right
        self._parent = parent
    
    @property
    def key(self):
        return self._key    
    
    @key.setter
    def key(self, value):
        self._key = value
        
    @key.deleter
    def key(self):
        del self._key
    
    @property
    def left(self):
        return self._left
        
    @left.setter
    def left(self, value):
        self._left = value
        
    @left.deleter
    def left(self):
        del self._left
        
    @property
    def right(self):
        return self._right    
    
    @right.setter
    def right(self, value):
        self._right = value
        
    @right.deleter
    def right(self):
        del self._right
        
    @property
    def parent(self):
        return self._parent
        
    @parent.setter
    def parent(self, value):
        self._parent = value
        
    @parent.deleter
    def parent(self):
        del self._parent
        
        
class BST(object):
    
    def __init__(self):
        self._root = None
        self.size = 0
    
    @property
    def root(self):
        return self._root
        
    @root.setter    
    def root(self, node):
        self._root = node
        
    
    def insert(self, number, parentnode=None, within_k = 0):
        
        if self.root is None:
            self.root = BinaryNode(number)
            self.size += 1
            return        
        if parentnode == None:
            parentnode = self.root

        if parentnode.key >= number:
            if parentnode.left is None:
                
                testnode = parentnode
                prev_val = None
                while testnode.parent is not None and testnode.parent.right is testnode:
                    testnode = testnode.parent
                    prev_val = testnode.key
                
                next_val = parentnode.key
                if (prev_val is None or prev_val <= number - within_k) and (number + within_k <= next_val):  
                    
                    parentnode.left = BinaryNode(value = number)
                    parentnode.left.parent = parentnode
                    self.size += 1
                else:
                    raise ValueError("Can't insert " + str(number) + " because of within_k rule.")
            else:
                self.insert(number, parentnode.left, within_k)
        else:
            if parentnode.right is None:
                
                prev_val = parentnode.key
                testnode = parentnode
                next_val = None
                while testnode.parent is not None and testnode.parent.left is testnode:
                    testnode = testnode.parent
                    next_val = testnode.key
                if prev_val <= number - within_k and (next_val is None or number + within_k <= next_val):  
                    
                    parentnode.right = BinaryNode(value = number)
                    parentnode.right.parent = parentnode
                    self.size += 1
                else:
                    raise ValueError("Can't insert " + str(number) + " because of within_k rule.")
            else:
                self.insert(number, parentnode.right, within_k)
                
    def find(self, number, node=None):
        if node is None:
            node = self.root
        
        if number == node.key:            
            return node
        elif number <= node.key:
            if node.left is None:
                raise ValueError(str(number) + " not found in BST.")
                return None
            else:
                return self.find(number, node.left)
        else:
            if node.right is None:
                raise ValueError(str(number) + " not found in BST.")
                return None
            else:
                return self.find(number, node.right)
                       
            
    def find_min(self, node=None):
        if node is None:
            node = self.root
        
        while not(node.left is None):
            node = node.left
        return node
    
    def find_max(self, node):
        if node is None:
            node = self.root
        while not(node.right is None):
            node = node.right
        return node
    
    def next_larger(self, node):
        if node.right is not None:
            return self.find_min(node.right)
        else:
            while node.parent is not None and node.parent.right is node:
                node = node.parent
            return node.parent
        
    def next_smaller(self, node):
        if node.left is not None:
            return self.find_max(node.left)
        else:
            while node.parent is not None and node.parent.left is node:
                node = node.parent
            return node.parent
            
          
    def delete(self, node):
        if node.left is None or node.right is None:
            if node.parent.right is node:
                node.parent.right = node.right or node.left
                if node.right is not None:
                    node.right.parent = node.parent
                elif node.left is not None:
                    node.left.parent = node.parent
            else:
                node.parent.left = node.right or node.left
                if node.right is not None:
                    node.right.parent = node.parent
                elif node.left is not None:
                    node.left.parent = node.parent
        else:
            nextnode = self.next_larger(node)          
            node.key,nextnode.key = nextnode.key,node.key
            self.delete(nextnode)
              
        

    
if __name__ == "__main__":
    
    array = [12,  0, 50, 97, 38, 89, 68, 71, 20, 29, 35, 39, 76, 63, 47, 17, 98, 15, 72, 81]
    x = BST()    
    for i in array:
        x.insert(i)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    