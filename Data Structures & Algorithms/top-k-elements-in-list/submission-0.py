class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        #key-val pairs, key = num of times and val = number    
        for num in nums:
            count[num] = 1+ count.get(num, 0)
        #append the vals to a list
        for num, cnt in count.items():
            freq[cnt].append(num)
        
        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res






        