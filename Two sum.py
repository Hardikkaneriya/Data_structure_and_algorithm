def twosum(data, result):
    dic ={}
    for i in range(len(l)):
        print(dic, i)
        a = result-data[i]
        if a in dic:
            return [i,dic[a]]
        else:
            dic[data[i]]=i


def threesum(l, result):
    data= sorted(l)
    for i in range(len(data)-2):
        l=i+1
        r=len(data)-1
        while (l<r):
            if data[i] + data[l] + data[r] == result :
                return (data[i] , data[l] , data[r])
            elif data[i] + data[l] + data[r] > result :
                r -= 1
            else:
                l += 1




l= [0,6,4,3,5]
s= 10
print(twosum(l,s))
print(threesum(l,s))