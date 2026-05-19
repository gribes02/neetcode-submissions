class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        map = {}
        most_frequent = []

        for num in nums:

            if num in map:
                map[num] += 1

            else: 
                map[num] = 0 
            
        for i in range(k):
            max_val = max(map, key=map.get)
            most_frequent.append(max_val)
            del map[max_val]

        return most_frequent