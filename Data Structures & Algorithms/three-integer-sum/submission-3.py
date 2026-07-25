class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        res=[]
        # print(nums)
        for i in range(0,len(nums)):
            # print(i,nums[i],li)
            si=i+1
            ei=len(nums)-1
            while si<ei:
                li=[nums[i]]
                # print(si,ei,nums[si],nums[ei],nums[i]+nums[si]+nums[ei])
                if nums[i]+nums[si]+nums[ei]==0:
                    li.append(nums[si])
                    li.append(nums[ei])
                    if li not in res:
                        res.append(li)
                    si=si+1
                    ei=ei-1
                elif nums[i]+nums[si]+nums[ei] >0:
                    ei=ei-1
                else:
                    si=si+1
        return res