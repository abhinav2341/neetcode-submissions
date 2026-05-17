class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm={}

        # nums = [3,4,5,6,3] 
        # target = 6

        for i in range(len(nums)):
            if nums[i] not in hm.keys():
                hm[nums[i]] = [i]
            else:
                hm[nums[i]].append(i)

        # print(hm)
        # # si=None
        # # ei=None
        for i in range(len(nums)):
            key=target-nums[i]
            if key in hm:
                for k in hm[key]:
                    if i != k:
                        return [i,k]        
        return []
                

