A=[1 ,5, 10, 20, 40, 80] 
n1=len(A)
B=[2,4,7,20,40,80] 
n2=len(B)
C=[20,40,34,78,56,80]
n3=len(C)
# a=[]
# last=-1234567890
# n=min(n1,n2,n3)
# if n1!=n:
#     if n2==n:
#         A,B=B,A
#     else:
#         A,C=C,A
# for i in range(n):
#     if A[i] in B:
#         if A[i] in C:
#             if last!=A[i]:
#                 a.append(A[i])
#                 last=A[i]
#     else:
#         continue
# print(a)
i = 0
j = 0
k = 0 
last = -12345678
res = []
while i < n1 and j < n2 and k < n3:
    if A[i] == B[j] == C[k]:
        if last != A[i]:
            res.append (A[i])
            last = A[i]
        i += 1
        j += 1
        k += 1
    
    elif min (A[i], B[j], C[k]) == A[i]:
        i += 1
    elif min (A[i], B[j], C[k]) == B[j]:
        j += 1
    else:
        k += 1
print(res)
