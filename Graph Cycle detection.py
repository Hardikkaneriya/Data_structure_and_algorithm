#detect a cycle for undirected graph
edges = [['a','c'] ,['a','d'] ,['d','e'] , ['c','d']]

graph = {}
for i,v in edges:
    if i not in graph:
        graph[i] = [v]
    else :
        graph[i].append(v)
    if v not in graph:
        graph[v] = [i]
    else:
        graph[v].append(i)

print(graph)

def dfs(start, visited , parent):
    visited.add(start)
    print(visited)
    for i in graph[start]:
        print(parent)
        print(i)
        if i in visited and parent != i:
            return True
        elif i in visited:
            continue
        else:
            dfs(i, visited, start)
    return False



visited= set()
ans = False
for i in graph.keys():
     if i not in visited:
        ans = dfs(i, visited , 'xy')
     print(ans)
     if ans == True:
         print('inside true loop')
         break
print(ans)

# check if directed graph is cyclic or not

edges = [[1,2] , [2,3] ,[3,4] , [1,5] ]
n=5
graph = { i : [] for i in range(1,n+1)}
print(graph)
for i,v in edges:
    graph[i].append(v)
print(graph)


visited = set()
def cyclic_path(graph,start, visited):
    stack=[start]
    while stack:
        print(stack)
        cur = stack.pop()
        print(cur)
        if cur in visited:
            return True
        visited.add(cur)
        print(visited)
        for i in graph[cur]:
            stack.append(i)
    return False
for i in range(1,n+1):
    if i not in visited:
        if cyclic_path(graph,i, visited) == False :
            pass
        else:
            print('True')


