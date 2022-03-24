def numRescueBoats(people,limit):

    people = sorted(people)
    lo = 0
    hi = len(people)-1
    boats = 0
    while lo <= hi:
        if people[lo] + people[hi] <= limit:
            lo += 1
            hi -= 1
        else:
            hi -= 1
        boats += 1
    return boats

people = [1,2]
limit = 3
print(numRescueBoats(people,limit))