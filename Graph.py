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
    if len(graph[start])==0:
        return
    for i in graph[start]:
        dfs_rec(graph,i)
    

dfs_rec(graph,10)
dfs_itr(graph,10)



#BFS (BREADTH FIRST SEARCH) 
graph = { 10 : [20,30,40,50],
         20:[500],500:[1000],100:[],200:[],1000:[],30:[100] ,40:[200],50:[60],60:[70],70:[]}

def bfs_itr(graph,start):
    queue=[start]
    while queue:
        cur= queue.pop()
        print(cur, end=" ")
        for i in graph[cur]:
            queue.insert(0,i)


bfs_itr(graph,10)

# ========================================= Leetcode Problems ==================================
#===============================================================================================
# code to check if given graph has a path from start to end for a given path or not
graph = { 
    100: [10],
    10:[20],
    20:[30],
    30:[40,60,70],
    40:[500,50],
    50:[60],
    60:[],
    70:[],
    500:[]
}

#using DFS
def path_or_not_dfs(graph,start,end):
    stack=[start]
    
    while stack:
        cur= stack.pop()
        for i in graph[cur]:
            if i == end :
                return True
            stack.append(i)
    return False

#using BFS approach
def path_or_not_bfs(graph,start,end):
    queue=[start]
    while queue:
        cur= queue.pop()
        if cur == end:
            return True
        for i in graph[cur]:
            queue.insert(0,i)
    return False

print(path_or_not_dfs(graph,100,500))
print(path_or_not_bfs(graph,100,500))



#### when there is a non directed graph given and we need to find if path is present or not then we need to implment visited set to exclude 
#### already visited elements

nondirected_graph = { 'a':['b','c'] , 'b':['d','f','a'] , 'c':['a'] , 'd':['b','g','i'] , 'e':['f','h'] , 'f':['b','e'] ,
                      'g':['d','h'] , 'h':['e','g'] , 'i':['d']}



start = 'a'
end = 'z'
stack = [start]
visited = set()
def dfs_path(graph):
    while stack:
        cur = stack.pop()
        print(cur)
        if cur not in visited:
            if cur == end :
                return True
            visited.add(cur)
        else :
            continue
        for i in nondirected_graph[cur]:
            stack.append(i)
    return False
print(dfs_path(graph))

#recursive approach
def dfs_path_rec(graph,start):
    if start == end :
        return True
    visited.add(start)
    for i in graph[start]:
       if i not in visited:
            if dfs_path_rec(graph , i) == True :
                return True
    return False

start = 'a'
end = 'g'
visited= set()
print(dfs_path_rec(nondirected_graph,start))

# ========== code to find the province (no of separated graphs when number of nodes and edges are given ========
#here we need to find the number of provinces (number of separate graphs)

n = 6
edges = [(1,2) ,(1,3) ,(4,5) ]

graph = { i : [] for i in range(1,n+1)}
print(graph)

for i,j in edges :
    graph[i].append(j)
    graph[j].append(i)
print(graph)

visited = set()
cnt = 0
def calculate_no_of_provinces(graph,start , visited ):
    print(start)
    if start in visited:
        return False
    visited.add(start)
    for i in graph[start]:
        calculate_no_of_provinces(graph, i , visited )
    return True




for i in range(1,n+1):
    if i not in visited:
        cnt += 1
    calculate_no_of_provinces(graph,i , visited )
print('count' , cnt)

