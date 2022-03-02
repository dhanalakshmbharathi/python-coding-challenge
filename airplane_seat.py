n=2
if(n==1):
    print(1)
if(n==2):
    print(0.5)
if(n>2):
    dp=[0] * (n+1)
    dp[1]=1
    dp[2]=0.5
    acc=1.5
    for i in range(3,n+1):
        dp[i]=(1/i)*acc
        acc+=dp[i]
    print(dp[-1])
    