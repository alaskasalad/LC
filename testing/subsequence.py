class Sol:
    def subsequence(self, s:str, t:str) -> bool:
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        # if it finds all the letters (order doesnt matter)
        # i should be the same number as the len of s 
        return i == len(s)
            
            
            
        
s = "ace"
t = "abcde"

a = Sol()
print(a.subsequence(s, t))
