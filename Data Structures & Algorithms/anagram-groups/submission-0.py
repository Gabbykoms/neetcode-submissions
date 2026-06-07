class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = {}
        for i in range(len(strs)):
            curr = str(sorted(strs[i]))
            if curr in hashmap:
                hashmap[curr].append(strs[i])
            else:
                hashmap[curr] = [strs[i]]
        print(list(hashmap.values()))
        return list(hashmap.values())
        