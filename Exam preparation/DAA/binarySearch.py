""" 
1) Start
2) Read the search element from the user.
3) Find the middle element in the sorted array.
4) Compare the middle element with the search element.
5) If middle element is the search element, then return "Element has been found"
6) Else, 
    a) if middle element > search element:
        Then go to step 3 for the right sub list of the middle element.
    b) else:
        Go to step 3 for the left sub list of the middle element.
7) Repeat this until left>right 
"""

def binarySearch(a,l,r,key):
    m = int((l+r)/2);
    if(l>=r):
        print("The element was not found.");
    else:
        if(a[m]==key):
            print("The element has been found.");
        elif(key>a[m]):
            return binarySearch(a,l,m-1,key);
        else:
            return binarySearch(a,m+1,r,key);
    
arr = [12, 25, 33, 37, 48, 57, 86, 92];

binarySearch(arr,0,7,37);
