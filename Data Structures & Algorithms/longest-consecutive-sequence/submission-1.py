class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0 : return 0;
        hashset = set(nums)
        maxTill = 1
        for num in nums:
            if num-1 not in hashset:
                current = num+1
                while(current in hashset):
                    current+=1
                maxTill = max(maxTill, current-num)
        return maxTill