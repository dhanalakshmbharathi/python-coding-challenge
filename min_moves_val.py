def minRemoveToMakeValid( s: str) -> str:
        nrOpen = 0
        final = []
        for c in s:
            if c == '(':
                nrOpen += 1
                final.append(c)
            elif c == ')':
                if nrOpen > 0:
                    nrOpen -= 1
                    final.append(c)
            else:
                final.append(c)
        
        sol = ''
        for c in final[::-1]:
            if c == '(' and nrOpen > 0:
                nrOpen -= 1
            else:
                sol += c
        return sol[::-1]

w="lee(t(c)o)de)"
print(minRemoveToMakeValid(w))