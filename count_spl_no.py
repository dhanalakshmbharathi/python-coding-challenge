def gcd(a,b):
    assert int(a)==a and int(b)==b ,"This number must be integer only"
    if(a<0):
        a=-1*a
    if(b<0):
        b=-1*a
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
def product_digits_quartic(n):
    s=0
    product = 1
    while (n != 0):
        product = product * (n % 10)
        s=s+pow((n%10),4)
        n = n // 10
    return product,s
def special_number(n):
    c=0
    for ele in range(1,n+1):
        temp=product_digits_quartic(ele)
        a=temp[0]
        b=temp[1]
        k=gcd(a,b)
        if k>1:
            c+=1
    print(c)
T=int(input())
for i in range(T):
    n=int(input())
    special_number(n)