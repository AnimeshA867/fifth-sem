def selectionSort(arr):
    for j in range(len(arr) - 1):
        # Find the minimum element in the remaining unsorted array
        minimum_index = j
        for i in range(j + 1, len(arr)):
            if arr[i] < arr[minimum_index]:
                minimum_index = i
                
        # Swap the found minimum element with the first element
        arr[j], arr[minimum_index] = arr[minimum_index], arr[j]
        
        print(arr)

def main():
    arr = [25, 57, 48, 37, 12, 92, 86, 33]
    selectionSort(arr)

if __name__ == "__main__":
    main()
