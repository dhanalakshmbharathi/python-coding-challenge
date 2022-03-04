def isValid( s: str):
        stack = []
        for i in s:
            if i in {"(", "[", "{"}:
                stack.append(i)
            else:
                if not stack:
                    return False
                parenthesis = (i == ")" and stack[-1] == "(")
                brackets = (i == "]" and stack[-1] == "[")
                braces = (i == "}" and stack[-1] == "{")
                if parenthesis or brackets or braces:
                    stack.pop()
                    continue
                return False
        return not stack


s = "()[]{}"
print(isValid(s))