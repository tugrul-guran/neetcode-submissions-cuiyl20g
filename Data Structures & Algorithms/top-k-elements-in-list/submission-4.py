class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            if num not in count:
                count[num] = 0

            count[num] += 1

        result = []
        for _ in range(k):
            next_num = max(count, key = lambda x : count[x])
            result.append(next_num)
            del count[next_num]

        return result