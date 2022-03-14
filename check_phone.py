def check(ph):
    ph = list(map(str, ph))
    op = []
    temp = []
    op.append(ph[0])
    for i in ph[1:]:
        for j in op:
            try:
                if j == i[:len(j)]:
                    if i not in op:
                        op.append(i)
                elif ' ' in j or '+' in j or '(' in j or ')' in j:
                    temp.append(j)
                elif j == i:
                    op.append(j)
            except:
                pass
    op = list(map(int, op))
    op = op + temp
    if len(op) > 1:
        return op
    else:
        return -1


