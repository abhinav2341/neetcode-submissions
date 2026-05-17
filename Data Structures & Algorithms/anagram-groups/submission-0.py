class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hm={}
        for i,s in enumerate(strs):
            sorted_s="".join(sorted(s.lower()))
        
            if sorted_s in hm:
                hm[sorted_s].append(i)
            else:
                hm[sorted_s]=[i]

        res=[]
        for i in hm:
            t=[]
            for j in hm[i]:
                t.append(strs[j])
            res.append(t)

        return res
