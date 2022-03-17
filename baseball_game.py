def calPoints( ops) -> int:

    score=[]
    sum=0
    for i in ops:
        try:
            sum+=int(i)
            score.append(int(i))
        except:
            if i=="C":
                sum-=score[-1]
                del score[-1]
            elif i=="D":
                lastscore= 2*(score[-1])
                sum+=lastscore
                score.append(lastscore)
            elif i=="+":
                lastscore= score[-1]+score[-2]
                sum+=lastscore
                score.append(lastscore)
    return sum


ops = ["5","2","C","D","+"]
print(calPoints(ops))




