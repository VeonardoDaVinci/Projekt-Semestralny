# -*- coding: utf-8 -*-
import heapq
import pickle

s = open("lorem.txt",'r')
string = s.read()
s.close()


def textFreq(text):
    freq = {}
    for i in range(len(text)):
        if(text[i] in freq):
            a = freq[text[i]]
            a += 1
            freq[text[i]] = a
        else:
            freq.fromkeys(text[i])
            freq[text[i]] = 1
    return freq

def printTree(tree,depth = 0):
    value = tree[0]
    child0 = tree[1] if(len(tree)>=2) else None
    child1 = tree[2] if(len(tree)>=3) else None
    print('    '*depth,value)
    if(child0 != None):
        printTree(child0, depth+1)
    if(child1 != None):
        printTree(child1, depth+1)

textFreq(string)
freq = textFreq(string)
keys = list(freq.keys())
values = list(freq.values())
frequencies = list(zip(values,keys))


def makeTree(frequency):
    heap = []
    for i in frequency:
        heapq.heappush(heap,[i])
    while(len(heap)>1):
        child0 = heapq.heappop(heap)
        child1 = heapq.heappop(heap)
        freq0, label0 = child0[0]
        freq1, label1 = child1[0]
        freq = freq0 + freq1
        label = ''.join(sorted(label0 + label1))
        node = [(freq, label), child0, child1]
        heapq.heappush(heap, node)
    return(heap.pop())
    
tree = makeTree(frequencies)
printTree(tree)
def walkTree(codeTree, codeMap, codePrefix):
    if(len(codeTree)==1):
        frequency, label = codeTree[0]
        codeMap[label] = codePrefix
    else:
        value, child0, child1 = codeTree
        walkTree(child0, codeMap, codePrefix + "0")
        walkTree(child1, codeMap, codePrefix + "1")
    

def makeCodeMap(codeTree):
    codeMap = dict()
    walkTree(codeTree, codeMap, '')
    print(codeMap)
    return codeMap

makeCodeMap(makeTree(frequencies))

def code(message, frequencies):
    codeMap = makeCodeMap(tree)
    return ''.join([codeMap[letter] for letter in message])

encodedmessage = code(string,frequencies)
encodedbinary = int(encodedmessage,2)

w = open("encoded.txt",'wb')
pickle.dump(encodedbinary,w)
w.close()

w = open("encoded.txt",'rb')
encodedbinary = pickle.load(w)
#encodedbinary = w.read()
encodedbinary = bin(encodedbinary)
encodedbinary = encodedbinary[2:]

def zcode(encodedMessage, frequencies):
    codeTree = entireTree = tree
    decodedLetters = []
    for digit in encodedMessage:
        if (digit == '0'): 
            codeTree = codeTree[1]
        else:
            codeTree = codeTree[2]
        
        if (len(codeTree)==1):
            frequency, label = codeTree[0]
            decodedLetters.append(label)
            codeTree = entireTree
    return ''.join(decodedLetters)

zcode((encodedmessage),frequencies)
decodedmessage = zcode((encodedmessage),frequencies)

w.close()

print(decodedmessage)