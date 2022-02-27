
        
n=3       
        
a, b, c = 0, 1, 2
while (n > 2):
    a, b = b, c
    c = a + b
    n -=1
print(c)