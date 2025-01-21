from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = Counter(nums)
        max_freq = max(a.values())
        buckets = [[] for _ in range(max_freq + 1)]

        for num, count in a.items():
            buckets[count].append(num)

        result =  []
        for i,v in enumerate(reversed(buckets)):
            if v and len(result) < k:
                result.extend(v)
        return result

solution = Solution()  # Create an instance of the Solution class
solution.topKFrequent([2,1,1,4,3,2,1,3],2)
