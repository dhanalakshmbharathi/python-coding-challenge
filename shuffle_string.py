
s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
new_list=[None]*len(s)
for i in range(len(indices)):
    new_list[indices[i]]=s[i]
print ( ''.join(new_list))
