"""Given an integer array nums and an integer k, return the k most
 frequent elements. You may return the answer in any order."""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_of_frequent = {i:0 for i in nums}
        for i in range(len(nums)):
            if nums[i] in dict_of_frequent:
                dict_of_frequent[nums[i]] +=1

        dict_of_frequent = sorted(dict_of_frequent.items(), key=lambda x: x[1])
        answer = []
        for i in range(k):
            answer.append(dict_of_frequent.pop()[0])

        return answer