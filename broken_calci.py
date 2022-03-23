def brokenCalc(startValue: int, target: int) -> int:
    if startValue>target:
        return startValue-target
    total_steps=0
    while target!=startValue:
        if target<startValue:
            total_steps+=startValue-target
            target=startValue
        elif target%2==1:
            total_steps+=1
            target+=1
        else:
            target//=2
            total_steps+=1
    return total_steps


startValue = 2
target = 3
print(brokenCalc(startValue,target))