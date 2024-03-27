#graph Logic
#for each start,end point check if that is available in dic if 
#create an empty list in dic and then append start and end point in it
def graph(edges):
    graph={}
    for start,end in edges:
        if start not in graph:
            graph[start]=[]
        if end not in graph:
            graph[end]=[]
        graph[start].append(end)
        graph[end].append(start)
    return graph

edges=[['i','j'],['i','k'],['l','m'],['k','m']]
graph(edges)
        
