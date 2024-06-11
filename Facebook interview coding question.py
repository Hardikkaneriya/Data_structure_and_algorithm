'''
Find the sum of all arrays multipling the nums by level they are at [1,[1,1,[2]],6,[8]].
'''

l= [1,[1,1,[2]],6,[8]]
sm=0
pos=1


def dfs(l,pos,sm):
    if isinstance(l,int):
        return pos * l
    else :
        for i in l:
            sm= dfs(i,pos+1,sm)
    return sm

for i in l:
    sm += dfs(i,pos,sm)

print(sm)
