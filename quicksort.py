def quicksort(l):
    if len(l)<=1:
        return l
    left = []
    right = []
    for i in l[1:]:
        if i<=l[0]:
            left.append(i)
        else:
            right.append(i)
    return quicksort(left) + [l[0]] + quicksort(right)
    
    
    
# in-place version
def quicksort_in(l,a=None,b=None):
    if a == None:
        a = 0
    if b == None:
        b = len(l) - 1
    if b-a <= 0:
        return
    i = a+1
    j = b
    while(j-i>=0):
        while(i<=b and l[i]<=l[a]):
            i +=1
        while(l[j]>l[a]):
            j -=1
        if i<j:
            l[i],l[j] = l[j],l[i]
    l[a],l[j] = l[j],l[a]
    quicksort_in(l,a,j-1)
    quicksort_in(l,j+1,b)
    
