# -*- coding: utf-8 -*-
class TNode():
    def __init__(self):
        self.left = None
        self.right = None 
        self.key = None

#Liczba znaków w kodzie
n = 6

root = TNode()
def cypher():
    for i in range(n):
        s = input()
        b = input()
        p = root
        for j in range(len(b)):
            if(b[j] == '0'):
                if(p.left == None):
                    p.left = TNode()
                p = p.left            
            else:
                if(p.right == None):
                    p.right = TNode()
                p = p.right
        p.key = s
        print(p.key)
    
def decypher():
    code = input()
    p = root
    for i in range(len(code)):
        if(code[i] == '0'):
            p = p.left
        else:
            p = p.right
        if(p.left == None):
            print(p.key)
            p = root
        
cypher()
decypher()