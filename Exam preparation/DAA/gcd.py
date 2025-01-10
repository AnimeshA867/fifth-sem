def gcd(a,b):
    if(a==0):
        return b;
    else:
        return gcd(b%a,a);
    
    

def main():
    a= int(input("Enter any number a:"))
    b= int(input("Enter any number b:"))

    print(gcd(a,b));

if __name__=="__main__":
    main()