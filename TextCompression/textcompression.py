# -*- coding: utf-8 -*-
import heapq
import pickle


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

def code(message, frequencies):
    codeMap = makeCodeMap(tree)
    return ''.join([codeMap[letter] for letter in message])

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

f = input("Podaj nazwę pliku tekstowego (wraz z rozszerzeniem):")
file = open(f,'r')
string = file.read()
file.close()

#Uzyskiwanie częstoliwoci występowania znaków
freq = textFreq(string)
keys = list(freq.keys())
values = list(freq.values())
frequencies = list(zip(values,keys))

#Uzyskiwanie drzewa Huffmana
tree = makeTree(frequencies)
print("Drzewo Huffmana stworzone na podstawie podanego pliku:\n")
printTree(tree)
print("Mapa częstotliwosci występowania znaków:\n")
encodedmessage = code(string,frequencies)

#Dodanie 'kontrolnej' jedynki przed zakodowaną wiadomoscią
encodedmessage = '1'+encodedmessage
encodedbinary = int(encodedmessage,2)
print("Zakodowana wiadkomosc:\n")
print(bin(encodedbinary)[3:])
plik = input("Podaj nazwę pliku do którego chcesz zapisać skompresowane dane (wraz z rozszerzeniem):")
w = open(plik,'wb')
pickle.dump(encodedbinary,w)
w.close()

w = open(plik,'rb')
encodedbinary = pickle.load(w)
encodedbinary = bin(encodedbinary)
encodedbinary = encodedbinary[3:]

decodedmessage = zcode((encodedbinary),frequencies)
w.close()
zap = input("Podaj nazwę pliku do którego chcesz zapisać zdekompresowane dane (wraz z rozszerzeniem):")
z = open(zap,"w")
z.write(decodedmessage)
z.close()
print("Zdekodowana wiadomosc:\n")
print(decodedmessage)