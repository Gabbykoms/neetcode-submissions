class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        

        sorted_dict = sorted(hashmap.items(), key=lambda x: x[1], reverse=True)
        print(sorted_dict)

        res = []
        for i in range(k):
            res.append(sorted_dict[i][0])
        
        print(res)

        return res

        

        
        
        

       
        


        