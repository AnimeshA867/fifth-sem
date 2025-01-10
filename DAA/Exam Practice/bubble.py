def bubbleSort(arr):
    n=len(arr);
    
    for i in range(n-1):
        for j in range(n-i-1):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j];
                
    return arr;

def insertionSort(arr):
    n=len(arr);
    for i in range(1,n):
        key=arr[i];
        j=i-1;
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1;
        arr[j+1]=key
            
    
def swap(arr,a,b):
    arr[a],arr[b]= arr[b],arr[a];
def selectionSort(arr):
    n= len(arr);
    
    for i in range(n):
        p=i;
        for j in range(i+1,n):
            if(arr[j]<arr[p]):
                p=j;
        swap(arr,i,p)
arr = [40, 65, 19, 58, 36, 11, 92, 70, 97, 51]
insertionSort(arr)
print(arr)