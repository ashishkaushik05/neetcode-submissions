class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftRun = []
        currentProd = 1
        for num in nums:
            leftRun.append(currentProd)
            currentProd *= num
        currentProd = 1
        rightRun = []
        nums.reverse()
        for num in nums:
            rightRun.append(currentProd)
            currentProd*=num
        result = []
        rightRun.reverse()
        for i in range(len(nums)):
            result.append(leftRun[i]* rightRun[i])
        return result