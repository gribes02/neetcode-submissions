class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        map = {}

        anagram_list = []

        for i, s in enumerate(strs):
            sorted_s = ''.join(sorted(s))

            if sorted_s in map:
                map[sorted_s].append(s)

            else: 
                map[sorted_s] = [s] 

        for key, value in map.items():
            anagram_list.append(value)
            
        return anagram_list