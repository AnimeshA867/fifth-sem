def mergeSort(arr):
    if(len(arr)<=1):
        return arr;
    
    mid=len(arr)//2;
    
    leftSide = arr[:mid];
    rightSide =arr[mid:];
    
    sortedLeft= mergeSort(leftSide);
    sortedRight= mergeSort(rightSide);
    
    return merge(sortedLeft, sortedRight);

def merge(left, right):
    i=0;
    j=0;
    result= [];
    
    while (i<len(left) and j<len(right)):
        if(left[i]>right[j]):
            result.append(right[j]);
            j+=1;
        else:
            result.append(left[i]);
            i+=1;
    
    
    while(i<len(left)):
        result.append(left[i]);
        i+=1;
    
    while(j<len(right)):
        result.append(right[j]);
        j+=1;
    
    return result;

arr = [12, 25, 33, 37, 48, 57, 86, 92]
sorted_arr = mergeSort(arr)
print(sorted_arr)

