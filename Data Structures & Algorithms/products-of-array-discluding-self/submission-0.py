class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
            
        lprod=[1]*len(nums)
        rprod=[1]*len(nums)

        for i in range(0,len(nums)):
            # print(i,lprod,nums)
            if i == 0:
                lprod[i]=1
            else:
                lprod[i]=lprod[i-1]*nums[i-1]

        # print(lprod)

        for i in range(len(nums)-1,-1,-1):
            if i == (len(nums))-1:
                rprod[i]=1
            else:
                rprod[i]=rprod[i+1]*nums[i+1]

        # print(rprod)

        output=[]
        for i in range(0,len(nums)):
            output.append(lprod[i]*rprod[i])

        return output