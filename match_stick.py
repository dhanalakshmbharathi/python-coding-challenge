def makesquare( matchsticks) :
        sum_len = sum(matchsticks)
        if not sum_len % 4:
            target = sum_len // 4
            if max(matchsticks) <= target:
                matchsticks.sort(reverse=True)
                len_matchsticks = len(matchsticks)
                len_matchsticks1 = len_matchsticks - 1
                sides = (0, 0, 0, 0)
                combs = {sides}
                idx = 0
                while combs and idx < len_matchsticks:
                    new_combs = set()
                    for a, b, c, d in combs:
                        if a + matchsticks[idx] <= target:
                            new_combs.add((a + matchsticks[idx], b, c, d))
                        if b + matchsticks[idx] <= target:
                            new_combs.add((a, b + matchsticks[idx], c, d))
                        if c + matchsticks[idx] <= target:
                            new_combs.add((a, b, c + matchsticks[idx], d))
                        if d + matchsticks[idx] <= target:
                            new_combs.add((a, b, c, d + matchsticks[idx]))
                    combs = new_combs
                    if (idx == len_matchsticks1 and
                            (target, target, target, target) in combs):
                        return True
                    idx += 1
        return False

print(makesquare(matchsticks = [1,1,2,2,2]))
print(makesquare(matchsticks = [3,3,3,3,4]))