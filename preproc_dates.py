def preprocess(ip, n):
    lib = {'Jan': "1",
           'Feb': "2",
           'Mar': "3",
           'Apr': "4",
           'May': "5",
           'Jun': "6",
           'Jul': "7",
           'Aug': "8",
           'Sept': "9",
           'Oct': "10",
           'Nov': "11",
           'Dec': "12"}
    op1=[]
    op = []
    for i in ip:
        temp = i.split()
        date = temp[0][:-2]
        month = temp[1]
        year = temp[2]
        op1.append(year)
        op1.append(lib[month])
        op1.append(date)
        op.append('-'.join(op1))
    return op


ip=["1st Mar 1972","2nd Jan 2000"]
print(preprocess(ip,2))