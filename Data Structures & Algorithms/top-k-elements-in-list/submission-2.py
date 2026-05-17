class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        def insert(arr,i,val):
            if i == len(arr):
                return arr
            t=arr[i]
            arr[i]=val
            return insert(arr,i+1,t)

        hm = {}
        freq = [None]*k

        for i in range(len(nums)):
            if nums[i] not in hm.keys():
                hm[nums[i]] = 1
            else:
                hm[nums[i]]+=1

        for i in hm:
            for k,val in enumerate(freq):
                if val is None:
                    freq=insert(freq,k,i)
                    break
                if hm[val] < hm[i]:
                    freq=insert(freq,k,i)
                    break
        
        return freq