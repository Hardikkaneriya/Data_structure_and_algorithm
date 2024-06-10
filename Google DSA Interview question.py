'''
Given a network of routers (list of tuples representing coordinates of each router), a source (index in the routers list), a destination and a wireless range limit of the source, determine if a message broadcast from router at index source will reach the router at index destination.

Sample input: [(0,0),(0,8),(0,17),(11,0)], wireless range = 10, source = 0, destination = 3
'''

routers = [(0,0),(0,8),(0,17),(11,0)]
range_limit = 10
source = 0
dest = 50

def trasmit_msg(routers, source, dest, range_limit):
    network = {v:[] for v in range(len(routers))}
    def get_distance(s , d):
        x= (s[0] - d[0])*2
        y= (s[1] - d[1])*2
        return x+y
    for i in range(len(routers)):
        for j in range(i+1, len(routers)):
            d = get_distance(routers[i], routers[j])
            if d <= range_limit: #was told to assume this method return distance between two routers
                network[i].append(j)
                network[j].append(i)
    print(network)



    visited = set()
    def dfs(s):
        if s == dest:
            return True
        visited.add(s)
        for r in network[s]:
            if r not in visited:
                if dfs(r):
                    return True
        return False

    return dfs(source)

print(trasmit_msg(routers, source, dest, range_limit))
