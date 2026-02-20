class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        max_sum = 0
        for pair_min in nums[::2]:
            max_sum += pair_min
        return max_sum

# Runtime: 28 ms, Beats 41.12%
# Memory: 21.48 MB, Beats 70.62%
