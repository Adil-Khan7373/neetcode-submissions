class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_s={}
        for i in s:
            if i in freq_s:
                freq_s[i]+=1
            else:
                freq_s[i]=1
        freq_t={}
        for j in t:
            if j in freq_t:
                freq_t[j]+=1
            else:
                freq_t[j]=1
        if freq_s != freq_t:
            return False
        return True
        

