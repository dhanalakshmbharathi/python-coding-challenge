def strongPasswordChecker(password: str) -> int:
        count = 0
        lo = up = nu = 1
        flag = 1
        rep = 1
        if len(password) < 6:
            return 6 - len(password)
        else:
            repeat = ''
            for i in password:
                if i == repeat:
                    rep += 1
                    if rep >= 3:
                        count += 1
                        rep = 0
                    if count == 1:
                        if lo != 0:
                            lo = 0
                        elif up != 0:
                            up = 0
                        elif nu != 0:
                            nu = 0
                    if count == 2:
                        if lo != 0:
                            lo = 0
                        elif up != 0:
                            up = 0
                        elif nu != 0:
                            nu = 0
                    if count == 3:
                        if lo != 0:
                            lo = 0
                        elif up != 0:
                            up = 0
                        elif nu != 0:
                            nu = 0
                            
                elif ord(i) >= 65 and ord(i) <= 90:
                    up = 0
                elif ord(i) >= 97 and ord(i) <= 122:
                    lo = 0
                elif ord(i) >= 48 and ord(i) <= 57:
                    nu = 0

                if i != repeat:
                    rep = 1
                
                if i == repeat and rep > 2:
                    count = 1
                elif i == repeat and rep > 2:
                    count = 1
                repeat = i
            if rep >= 3:
                        count += 1
            if len(password) > 20:
                return len(password) - 20 + lo + up + nu + count
            else:
                return lo + up + nu + count

print(strongPasswordChecker("1111111111"))