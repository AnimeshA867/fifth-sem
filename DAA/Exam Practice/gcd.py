""" 
1) Read two elements a and b from the user
2) If a==0:
    return a;
3) Else:
   r=a%b;
   a=b;
   b=r;
    
"""

def gcdIt(a,b):
    if(b==0):
        return a;
    else:
        while(b!=0):
            
            a,b=b,a%b
    
    return a

def gcd(a,b):
    if(b==0):
        return a;
    else:
        return gcd(b,a%b)
print(gcd(11,3))