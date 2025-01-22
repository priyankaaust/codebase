class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for i, num in enumerate(nums):
            left = target - num
            if left in res:
                return [i,res[left]]
            res[num] = i
            
                
        return []
