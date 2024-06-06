# write a code to perform all possible combination of valid parenthesses


n= 3
res=[]

def dfs(left, right , s):
    if left == n and right == n :
        res.append(s)
        return

    if left < n :
        dfs(left+1,right , s + '(')

    if right < left :
        dfs(left, right+1 , s + ')')

print(dfs(0,0,''))
print(res)


## output
'''
['((()))', '(()())', '(())()', '()(())', '()()()']
'''
