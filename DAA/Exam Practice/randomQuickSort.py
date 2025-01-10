import random;
def swap(arr,a,b):
    arr[a], arr[b]= arr[b],arr[a];
    
def randomizedPartition(arr,l,r):
    k=random.randint(l,r);
    
    swap(arr,l,k);
    
    return partition(arr,l,r);
    
def quickSort(arr,l,r):
    if (l < r):
        p=randomizedPartition(arr,l,r);
        quickSort(arr,l,p-1);
        quickSort(arr,p+1,r);
    
def partition(arr,l,r):
    x=l+1;
    y=r;
    pivot = arr[l];
    
    while x<=y:
        while x<=y and arr[x]<=pivot:
            x+=1;
        while arr[y]>pivot:
            y-=1
        if x<y:
            swap(arr,x,y);
            
    swap(arr,l,y);
    
    return y;

arr = [40, 65, 19, 58, 36, 11, 92, 70, 97, 51]
quickSort(arr, 0, len(arr) - 1)
print(arr)