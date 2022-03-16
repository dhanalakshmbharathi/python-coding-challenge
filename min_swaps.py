def minSwaps(s: str) -> int:

    swaps = 0
            
    opening_total = 0
    closing_total = 0
    
    for letter in s:
        if letter == ']':
            closing_total += 1
        if letter == '[':
            opening_total += 1
        if closing_total > opening_total:
            swaps += 1
            closing_total -= 1
            opening_total += 1
        
    return swaps

print(minSwaps(s = "]]][[["))