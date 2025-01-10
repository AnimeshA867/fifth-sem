""" 
There are two ways:
1) Iteration method
2) Divide and conquer method


"""

def minmax(a,l,r):
    if(l>r):
        return;
    
    if(l==r):
        return (a[l],a[r]);
    elif(l==r-1):
        if(a[l]>a[r]):
            return (a[l],a[r]);
        else:
            return (a[r],a[l]);
    else:
        m = int((l+r)/2);
        (max,min)=minmax(a,l,m);
        (max1, min1)= minmax(a,m+1,r);
        
        if(max<max1):
            max=max1;
        
        if(min>min1):
            min=min1;
            
        return (max,min);
    

arr= [12, 25, 33, 37, 48, 57, 86, 92];

print(minmax(arr,0,7));
