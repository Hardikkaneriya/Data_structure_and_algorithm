#implement bubble sort
#time complexity O(n*2)
l=[1,5,3,2,10,8]
def bubble_sort(l):
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[j-1] > l[j]:
                l[j-1] , l[j] = l[j] ,l[j-1]
    print(l)
bubble_sort(l)

# selection sorting 
#time complexity O(n*2)
l=[6,5,1,2,10,8]
def selection_sort(l):
    for i in range(len(l)):
        curr_index = i 
        for j in range(i+1 , len(l)):
            if l[j] < l[curr_index] :
                curr_index = j
        l[i] , l[curr_index] = l[curr_index] , l[i]
    print(l)
selection_sort(l)

#quick sorting 
#time complexity O(n * 2) in worst case but in average case it is O(nlog(n))

l=[6,5,1,2,10,8]
def quick_sort(l):
    if len(l) <= 1:
        return l
    else:
        pivot = l.pop()
    greater = []
    lower =[]

    for i in l:
        if i > pivot :
            greater.append(i)
        else:
            lower.append(i)    
    return quick_sort(lower) + [pivot] + quick_sort(greater)        
quick_sort(l)


#=============MERGE SORTING =================#
## time complexity = O(nlog(n))


def merge_sort(a):
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    left= a[:mid]
    right = a[mid:]
    left= merge_sort(left)
    right= merge_sort(right)

    return merge_sort_two_sorted_lists(left, right)
    

def merge_sort_two_sorted_lists(l,g):
    sorted_list=[]
    left = len(l)
    right = len(g)

    i=j=0

    while i < left and j < right:
        if l[i] < g[j] :
            sorted_list.append(l[i])
            i += 1
        else:
            sorted_list.append(g[j])
            j += 1
    while i < left:
        sorted_list.append(l[i])
        i += 1
    while j < right:
        sorted_list.append(g[j])
        j+=1
    return sorted_list

a=[6,5,1,2,10,8]
print(merge_sort(a))
