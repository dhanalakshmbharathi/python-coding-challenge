def wordBreak( line, dictionary) -> bool:
    dp =[False for i in range(len(line)+1)]
    dp[len(line)]=True

    for  i in range(len(line)-1,-1,-1):
        for w in dictionary:
            if(i+len(w)<=len(line) and line[i:i+len(w)]==w):
                dp[i]=dp[i+len(w)]
            if dp[i]:
                break
    return dp[0]



s="catsandog"
dict=["cats","dog","sand","and","cat"]
print(wordBreak(s,dict))