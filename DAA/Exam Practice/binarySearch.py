""" 
1) Start
2) Read the search element from the user
3) Find the mid element from the array
4) Compare the mid element with the search element, if both are same, return "Element found" else continue;
5) Compare the mid element with the search element to find out whether the mid element is greater or smaller than the search element.
5) If mid element is greater than the search element, repeat from step 3 for right sub-list.
6) If mid element is smaller than the search element, repeat from step 3 for left sub-list.
7) Continue this until we find the element or there is only one element in the sublist.
8) If there is only one element in the sublist and the element is not the key, return "Element not found"
9) Stop
"""

def binarySearch(arr,left,right,key):
    mid=(left+right)//2;
    midElement= arr[mid];
    if(left>=right):
        print("Element was not found.")
        return;
    if(midElement==key):
        print("Element has been found.")
        return;
    else:
        if(midElement>key):
            return binarySearch(arr,left,mid-1,key);
        else:
            return binarySearch(arr,mid+1,right,key);
        
arr = [1,2,3,4,5,6,7,8,9];
binarySearch(arr,0,len(arr)-1,-2)