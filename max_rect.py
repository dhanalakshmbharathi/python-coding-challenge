def maximalRectangle( mat) -> int:
    def LRIH(hist):
        n = len(hist)
        left = [0]*n
        left[0] = -1
        for i in range(1, n):
            j = i-1
            while j >= 0 and hist[j] >= hist[i]:
                j = left[j]
            left[i] = j
            
        right = [0]*n
        right[n-1] = n
        for i in range(n-2, -1, -1):
            j = i+1
            while j <= n-1 and hist[j] >= hist[i]:
                j = right[j]
            right[i] = j
        
        res = 0
        for i in range(n):
            curr = (right[i] - left[i] - 1) * hist[i]
            res = max(res, curr)
            
        return res
        
    
    
    m = len(mat)
    n = len(mat[0])
    
    for i in range(m):
        for j in range(n):
            mat[i][j] = int(mat[i][j])
            if i > 0:
                if mat[i][j] == 1:
                    mat[i][j] = 1 + mat[i-1][j]
    
    ans = 0
    for i in range(m):
        ans = max(ans, LRIH(mat[i]))
    
    return ans