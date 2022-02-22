n=3
# arr=[]
# for i in range(n+1):
#     ans=0
#     num=bin(i)
#     for j in num:
#         if(j=='1'):
#             ans+=1
#         else:
#             continue
#     arr.append(ans)
# print(arr)
        
dp=[0]*(n+1)
offset=1
for i in range(1,n+1):
    if(offset*2==i):  # to check if We've reached offset change(2,4,8,16)
        offset=i
    dp[i]=1+dp[i-offset]

print(dp)
    