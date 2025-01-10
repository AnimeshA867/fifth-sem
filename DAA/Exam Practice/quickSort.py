""" 
1) Start
2) Initialize two pointers left and right and a pivo element.
3) Compare both left(lelement) and right pointer(relement) with the pivot element
4) If lelement is less than pivot and relement is greater than pivot:
    a) Increment left pointer
    b) Decrement right pointer.
Else:
    a) Swap lelement and relement
5) If left>=right, swap pivot with either left or right element
6) 
"""
def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]
    
def quickSort(arr, l, r):
    if l < r:
        p = partition(arr, l, r)
        quickSort(arr, l, p - 1)  # Sort the left part
        quickSort(arr, p + 1, r)  # Sort the right part
        
""" def partition(arr, l, r):
    x = l + 1  # Start from the element next to the pivot
    y = r  # Start from the rightmost element
    p = arr[l]  # Choose the pivot as the first element
    
    while x <= y:
        # Move x to the right as long as arr[x] <= pivot
        while x <= y and arr[x] <= p:
            x += 1
        
        # Move y to the left as long as arr[y] > pivot
        while arr[y] > p:
            y -= 1
        
        # If x is still less than y, swap the elements
        if x < y:
            swap(arr, x, y)
    
    # Swap the pivot element with the element at index y
    swap(arr, l, y)
    return y
 """

def partition(arr,l,r):
    x=l+1;
    y=r;
    p=arr[l];
    while(x<=y):
        while arr[x]<=p:
            x+=1;
        while arr[y]>p:
            y-=1;
        
        if x<y:
            swap(arr,x,y);
    
    swap(arr,l,y);
    return y;
    
arr = [40, 65, 19, 58, 36, 11, 92, 70, 97, 51]
quickSort(arr, 0, len(arr) - 1)
print(arr)
