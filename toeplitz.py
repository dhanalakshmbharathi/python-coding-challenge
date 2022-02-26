
m=[[1,2],[2,2]]
# k=True
# for i in range(len(m)):
#     for j in range(len(m[0])):
#         if(i==0 or j==0):
#             continue
#         else:
#             if(m[i][j]!=m[i-1][j-1]):
#                 k=False
#             else:
#                 continue
# print(k)
k=True
rows = len(m)
cols = len(m[0])
for i in range(rows-1):
    if m[i][:cols-1] != m[i+1][1:cols]:
        k=False
print(k)

