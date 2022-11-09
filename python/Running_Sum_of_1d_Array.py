"""Given an array nums. We define a running sum of an
array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums."""
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        answer=list()
        current=0
        for i in nums:
            current+=i
            answer.append(current)
        return answer