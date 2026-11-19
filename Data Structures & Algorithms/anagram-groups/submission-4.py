class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = {}
        for i in range(len(strs)):
            curr = str(sorted(strs[i]))
            if curr in hashmap:
                hashmap[curr].append(strs[i])
            else:
                hashmap[curr] = [strs[i]]
        #print(list(hashmap.values()))
        return list(hashmap.values())

        #this is an O(m * nlogn) time complexity. m is longest string
        #it has O(n) space complexity
        #i go through the array and get a sorted string, create a new list 
        #as the values or add it to the existing list
        