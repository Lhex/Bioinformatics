from xml.dom.minicompat import NodeList
from _operator import indexOf
import time
def Composition(k, Text):
    Kmers = []
    for i in range(len(Text) - k + 1):
        kmer = Text[i:i+k]
        Kmers.append(kmer)
    return Kmers

# file = open("C://Users//Yap Xiu Ren//Downloads//dataset_197_3 (1).txt")
# # file = open("C://Users//Yap Xiu Ren//Downloads//dna_test.txt")
# all_lines = file.readlines()
# file.close()
#     
# k = int(all_lines[0].rstrip("\n"))
# DNA = all_lines[1].rstrip("\n")
# a = "\n".join(map(str, Composition(k, DNA)))
# 
# text_file = open("Output.txt", "w")
# text_file.write(a)
# text_file.close()

def Sequence(Strings):
    k = len(Strings[0])
    Genome = Strings[0]
    for i in range(1, len(Strings)):
        Genome += Strings[i][k - 1]
    return Genome

# file = open("C://Users//Yap Xiu Ren//Downloads//dataset_198_3.txt")
# all_lines = file.readlines()
# file.close()
# 
# DNA = []
# for i in range(len(all_lines)):
#     dna_line = all_lines[i].rstrip("\n")
#     DNA.append(dna_line)
# a = Sequence(DNA)
# text_file = open("Output.txt", "w")
# text_file.write(a)
# text_file.close()

def OverlapGraph(Strings):
    k = len(Strings[0])
    Nodes = []
    for i in range(len(Strings)):
        for j in range(len(Strings)):
            if i != j:
                if Strings[i][1:k] == Strings[j][0:k-1]:
                    Node = Strings[i] + " -> " + Strings[j]
                    Nodes.append(Node)
    return Nodes

# file = open("C://Users//Yap Xiu Ren//Downloads//dataset_198_10.txt")
# all_lines = file.readlines()
# file.close()
#  
# DNA = []
# for i in range(len(all_lines)):
#     dna_line = all_lines[i].rstrip("\n")
#     DNA.append(dna_line)
# # print('\n'.join(OverlapGraph(DNA)))
# a = '\n'.join(OverlapGraph(DNA))
# text_file = open("Output.txt", "w")
# text_file.write(a)
# text_file.close()

def DeBrujink(k, Text):
    Graph = []
    GraphOutput = []
    for i in range(len(Text) - k + 1 + 1):
        Graph.append(Text[i:i+k-1])
    for i in range(len(Graph)):
        if Graph[i] not in GraphOutput:
            GraphOutput.append(Graph[i])
    GraphMatrix = PathGraph(k, Text)
    SortedNode = sorted(GraphOutput)
    print("Nodes Sorted")
    NodesOutput = []
    for node in SortedNode:
        index = GraphOutput.index(node)
        NodeList = GraphMatrix[index]
        NodeOutput = []
        for i in range(len(NodeList)):
            for j in range(NodeList[i]):
                NodeOutput.append(GraphOutput[i])
        if len(NodeOutput) > 0:
            NodesOutput.append(node + " -> " + ",".join(sorted(NodeOutput)))
    return("\n".join(NodesOutput))

def PathGraph(k, Text):
    Graph = []
    GraphOutput = []
    GraphMatrix = []
    for i in range(len(Text) - k + 1 + 1):
        Graph.append(Text[i:i+k-1])
    for i in range(len(Graph)):
        if Graph[i] not in GraphOutput:
            GraphOutput.append(Graph[i])
    print(Graph)
    print(GraphOutput)
    print(len(GraphOutput))
    for i in range(len(GraphOutput)):
        iMatrix=[]
        for j in range(len(GraphOutput)):
            iMatrix.append(0)
        GraphMatrix.append(iMatrix)
    for i in range(1, len(Graph)):
        indexX = GraphOutput.index(Graph[i - 1])
        indexY = GraphOutput.index(Graph[i])
        GraphMatrix[indexX][indexY] += 1
        print(i)
    print("PathGraphDone")
    return GraphMatrix

# print(PathGraph(3, "TAATGCCATGGGATGTT"))
# print(PathGraph(4, "AAGATTCTCTAAGA"))
# print(DeBrujink(4, "AAGATTCTCTAAGA"))

# file = open("C://Users//Yap Xiu Ren//Downloads//dna_test.txt")
# file = open("C://Users//Yap Xiu Ren//Downloads//dataset_199_6 (4).txt")
# all_lines = file.readlines()
# file.close()
#    
# k = int(all_lines[0].rstrip("\n"))
# DNA = all_lines[1].rstrip("\n")
# print(k)
# print(DNA)
# a = DeBrujink(k, DNA)
# text_file = open("Output.txt", "w")
# text_file.write(a)
# text_file.close()

def DeBruijn(Patterns):
    k = len(Patterns[0])
    AdjacencyList = {}
    AdjacencyOutput = []
    # Set unique keys of patterns
    for Pattern in Patterns:
        AdjacencyList[Pattern[0:k-1]] = []
    # Put each pattern into the key corresponding to [0:k-1]
    for Pattern in Patterns:
        AdjacencyList[Pattern[0:k-1]].append(Pattern[1:k])
    print(AdjacencyList)
    for key in sorted(AdjacencyList):
        AdjacencyOutput.append(key + " -> " + ",".join(sorted(AdjacencyList[key])))
    return '\n'.join(AdjacencyOutput)
        
        
# file = open("C://Users//Yap Xiu Ren//Downloads//dna_test.txt")
# all_lines = file.readlines()
# file.close()
# DNA = []
# for i in range(len(all_lines)):
#     dna_line = all_lines[i].rstrip("\n")
#     DNA.append(dna_line)
# print(DNA)
# # print(DeBruijn(DNA))
# a = DeBruijn(DNA)
# text_file = open("Output.txt", "w")
# text_file.write(a)
# text_file.close()

def EulerianCycle(Graph):
    stack = []
    circuit = []
    for edge in Graph:
        if len(Graph[edge]) > 1:
            startingPosition = edge
    location = startingPosition
    stack.append(startingPosition)
    location = Graph[location].pop()
    while len(Graph[location]) > 0 or len(stack) > 0:
        if len(Graph[location]) > 0:
            stack.append(location)
            location = Graph[location].pop()
        else:
            circuit.append(location)
            location = stack.pop()
            
    circuit.append(location)
    circuit.reverse()
    outputCircuit = '->'.join(circuit)  
    return outputCircuit
        
#file = open("C://Users//Yap Xiu Ren//Downloads//bioinformatics_test.txt")
#all_lines = file.readlines()
#file.close()
#Graph = {}
#for i in range(len(all_lines)):
#    graph_line = all_lines[i].rstrip("\n")
#    node = graph_line.split(sep=" -> ")[0]
#    Graph[node] = []
#    neighbours = graph_line.split(sep=" -> ")[1]
#    for neighbour in neighbours.split(sep=","):
#        Graph[node].append(neighbour)
#print(EulerianCycle(Graph))
        
file = open("C://Users//Yap Xiu Ren//Downloads//bioinformatics_test.txt")
all_lines = file.readlines()
file.close()
Graph = {}
for i in range(len(all_lines)):
    graph_line = all_lines[i].rstrip("\n")
    node = graph_line.split(sep=" -> ")[0]
    Graph[node] = []
    neighbours = graph_line.split(sep=" -> ")[1]
    for neighbour in neighbours.split(sep=","):
        Graph[node].append(neighbour)
print(Graph)

def EulerianPath(Graph):
    
    nodes = []
    inNodes = []
    for key in Graph:
        nodes.append(key)
        nodes += Graph[key]
        inNodes += Graph[key]
    
    allNodes = list(set(nodes))
    oddNodes = {}
    index = 0
    while len(oddNodes) < 2:
        if allNodes[index] in Graph:
            degree = inNodes.count(allNodes[index]) - len(Graph[allNodes[index]])
        else:
            degree = inNodes.count(allNodes[index])
        if degree % 2 != 0:
            oddNodes[allNodes[index]] = degree
        index += 1
    
    for node in allNodes:
        if node not in Graph:
            Graph[node] = []
    
    stack = []
    circuit = []
    for key in oddNodes:
        if oddNodes[key] < 0:
            startingPosition = key
    location = startingPosition
    stack.append(startingPosition)
    location = Graph[location].pop()
    while len(Graph[location]) > 0 or len(stack) > 0:
        if len(Graph[location]) > 0:
            stack.append(location)
            location = Graph[location].pop()
        else:
            circuit.append(location)
            location = stack.pop()
            
    circuit.append(location)
    circuit.reverse()
    outputCircuit = '->'.join(circuit)  
    return outputCircuit

start_time = time.time()
print(EulerianPath(Graph))
print("--- %s seconds ---" % (time.time() - start_time))

        
        
        
        
        
        
        
        
        
        
        