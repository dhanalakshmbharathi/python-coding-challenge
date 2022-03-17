def scoreOfParentheses(s: str) -> int:
    stack = [[s, 1]]
    result, count = 0, 0
    while stack:
        curr, score = stack.pop()
        temp = ""
        for p in curr:
            temp += p
            if p=="(":
                count += 1
            else:
                count-=1
            if not count:
                if temp == "()":
                    result += score
                else:
                    stack.append([temp[1:-1], score*2])
                temp, count = "", 0
    return result


s = "((()))()"
print(scoreOfParentheses(s))