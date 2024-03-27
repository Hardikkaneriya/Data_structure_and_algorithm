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


def merge_sort(arr):
    if len(arr) <= 1:
        return

    mid = len(arr)//2

    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    merge_two_sorted_lists(left, right, arr)

def merge_two_sorted_lists(a,b,arr):
    len_a = len(a)
    len_b = len(b)

    i = j = k = 0

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            arr[k] = a[i]
            i+=1
        else:
            arr[k] = b[j]
            j+=1
        k+=1

    while i < len_a:
        arr[k] = a[i]
        i+=1
        k+=1

    while j < len_b:
        arr[k] = b[j]
        j+=1
        k+=1

if __name__ == '__main__':
    test_cases = [
        [10, 3, 15, 7, 8, 23, 98, 29],
        [],
        [3],
        [9,8,7,2],
        [1,2,3,4,5]
    ]

    for arr in test_cases:
        merge_sort(arr)
        print(arr)
