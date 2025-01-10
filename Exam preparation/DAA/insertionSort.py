""" 
Algorithms:
1) Start
2) Consider the first element to be sorted and rest to be unsorted.
3) Compare with the second element:
    a) If the second element < first element, insert the element in the correct position of thhe sorted portion.
    b) Else, leave it as it is.
4) Repeat step 2 and 3 until all the elements are sorted.
5) Stop    


"""

def insertionSort(arr):
    for i in range (1,len(arr)):
        temp = arr[i];
        j = i-1;
        
        while( j >=0 and  arr[j]>temp):
            arr[j+1]= arr[j];
            j-=1;
        
        arr[j+1]=temp;
        
        print(arr);
        

def main():
    arr = [25, 57, 48, 37, 12, 92, 86, 33]
    insertionSort(arr)

if __name__ == "__main__":
    main()