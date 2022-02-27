n = str(input('Enter number : '))
num_of_digits = len(n)
n = int(n)
number = []
for i in range(1,n+1):
    temp = " "
    bla = i
    while bla != 0:
        temp = str(bla % 2) + temp
        bla = int(bla / 2)
    if int(temp) > n:
        break
    number.append(int(temp))
    
count = 0
i = len(number)-1
while n != 0:
    if number[i] > n:
        i -= 1
    else:
        n = n - number[i]
        count += 1
print(count)