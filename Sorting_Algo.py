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

#quick sorting --> very efficient sorting algorithm
#time complexity O(nlog(n))

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
