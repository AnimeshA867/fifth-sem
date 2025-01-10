""" 
1) Start
2) Read the list of element from the user
3) If the length of list is 1, return the element as both min and max
4) If the length of list is 2, compare the first and second element. If first>second, return max=first and min=second else return max=second and min=first
5) If the length of list is greater than 2:
    a) Find the middle element
    b) Divide the list recursively into left sublist and right sublist and find the min and max from both sublist.
    c) Assign min and max of left sublist to be min1 and max1
    d) Assign min and max of right sublist to be min2 and max2
    e) If min1<min2, min=min1 else min=min2
    f) if max1>max1, max=max1 else max=max2
"""

def minMax(arr,left,right):
    if(left==right):
        return (arr[left],arr[right]);
    elif(left==right-1):
        return (arr[left],arr[right]) if arr[left]<arr[right] else (arr[right],arr[left])
    else:
        mid=(left+right)//2;
        (min1,max1)=minMax(arr,left,mid);
        (min2,max2)=minMax(arr,mid+1,right);
        min=min1 if min1<min2 else min2;
        max=max1 if max1>max2 else max2;
        return (min,max);
    
arr= [40, 65, 19, 58, 36, 11, 92, 70, 97, 51]
print(minMax(arr,0,len(arr)-1))