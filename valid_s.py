def validateStackSequences( pushed, popped ):
    s = []
    p = list(reversed(popped))
    for i in pushed:
        if i != p[-1]:
            s.append(i)
        else:
            p.pop()
            while len(s) and  s[-1] == p[-1]:
                s.pop()
                p.pop()
    
    return len(s) == 0

pushed = [1,2,3,4,5]
popped = [4,5,3,2,1]
print(validateStackSequences(pushed,popped))