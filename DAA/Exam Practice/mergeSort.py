""" 
1) Start
2) Read the elements from the user
3) Use recursion:
    Base case:
    If the lenght of the array is less than or equal to 1, return array.
    Recursion:
    a) Find the mid point of the array
    b) Find the pivot element at the middle of the array
    c) Store the elements less than pivot in array named leftArr.
    d) Store the element equal to the pivot in array named midArr.
    e) Store the elemetn more than pivot in array named rightArr.
    f) Return mergeSort(leftArr)+midArr+ mergeSort(rightArr)
"""

def mergeSort(arr):
    if(len(arr)<=1):
        return arr;
    mid=len(arr)//2;
    pivot=arr[mid]
    leftArr= [x for x in arr if x<pivot];
    midArr= [x for x in arr if x==pivot]
    rightArr=[x for x in arr if x>pivot]
    return mergeSort(leftArr)+midArr+mergeSort(rightArr)

print(mergeSort([40, 65, 19, 58, 36, 11, 92, 70, 97, 51]))