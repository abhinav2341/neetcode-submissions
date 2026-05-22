import math
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        hm={}

        for i in nums:
            hm[i]=1

        # print(2 in hm and hm[2]==1)



        # si=-(int(math.pow(10,9)))
        # ei=int(math.pow(10,9))

        si=min(nums)
        ei=max(nums)

        # si=-10
        # ei=100

        # print(si,ei,ei+1)

        maxcount=0
        cnt=0
        for i in range(si,ei+1):
            # print(i)
            if i in hm and  hm[i]==1:
                # print(i)
                cnt+=1
                maxcount=max(maxcount,cnt)
                print(cnt,maxcount)
            else:
                cnt=0

        # print('max',maxcount)
        return maxcount
        