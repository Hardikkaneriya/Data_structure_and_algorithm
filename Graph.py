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
        
#LINK TO UNDERSTAND DFS AND BFS 
# https://www.geeksforgeeks.org/difference-between-bfs-and-dfs/

#DFS (DEPTH SERACH FIRST) with iterative method and recursive method
graph = { 10 : [20,30,40,50],
         20:[], 30:[] ,40:[],50:[60],60:[70],70:[]}


def dfs_itr(graph,start):
    stack=[start]
    while stack:
        cur= stack.pop()
        print(cur)
        for i in graph[cur]:
            stack.append(i)

def dfs_rec(graph,start):
    print(start , end=' ')
    if len(graph[start]==0):
        return
    for i in graph[start]:
        dfs_rec(graph,i)
    

dfs_rec(graph,10)
dfs_itr(graph,10)
