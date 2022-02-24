nums1,nums2=[1,2],[3]
# nums=sorted(nums1+nums2)
# n=len(nums)
# if((n%2==0)):
#     m=(nums[int(n/2)]+nums[int(n/2)-1])/2
#     print(m)
# else:
#     k=int((n-1)/2)
#     print(nums[k])
a,b=nums1,nums2
if len(b)<len(a):
    a,b=b,a
t=len(a)+len(b)
h,k=t//2,True
l,r=0,len(a)
while k==True:
    i=(l+r)//2
    j=h-i-2
    aleft=a[i] if i>=0 else float("-infinity")
    aright=a[i+1] if i+1< len(a) else float("infinity")
    bleft=b[j] if j>=0 else float("-infinity")
    bright=b[j+1] if j+1< len(b) else float("infinity")
    if(aleft<=bright and bleft<=aright):
        if(t%2==0):
            print(min(aright,bright))
            k=False
        else:
            print(max(aleft,bleft)+min(aright,bright)/2)
            k=False
    elif(aleft>bright):
        r=i-1
    else:
        l=i+1
