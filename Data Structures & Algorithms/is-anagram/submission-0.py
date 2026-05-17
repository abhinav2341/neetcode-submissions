class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        
        sfreq = {}
        tfreq = {}
        
        for i in range(len(s)):
            if s[i] not in sfreq:
                sfreq[s[i]] = 1
            else:
                sfreq[s[i]] =  sfreq[s[i]] + 1
            if t[i] not in tfreq:
                tfreq[t[i]] = 1
            else:
                tfreq[t[i]] += 1
        
       
        for k in sfreq.keys():
            if k not in tfreq:
                return False
                
            if sfreq[k] != tfreq[k]:
                return False
                

        return True
        