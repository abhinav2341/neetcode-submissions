class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        j=1

        while i<len(numbers):
            if target-(numbers[i]+numbers[j]) == 0:
                return[i+1,j+1]
            elif target-(numbers[i]+numbers[j]) > 0:
                j=j+1
            else:
                i=i+1
                j=i+1
            if j==len(numbers):
                i=i+1
                j=i+1
        
        return []