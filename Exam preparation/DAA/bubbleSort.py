def bubbleSort(arr):
    n = len(arr);
    for i in range(0,n):
        for j in range(n-i-1):
            if(arr[j]>arr[j+1]):
                temp=arr[j];
                arr[j]=arr[j+1];
                arr[j+1]=temp;
            print(arr);     
    


def main():
    arr=[25,57,48,37,12,92,86,33];
    bubbleSort(arr);
    

if __name__=="__main__":
    main();
