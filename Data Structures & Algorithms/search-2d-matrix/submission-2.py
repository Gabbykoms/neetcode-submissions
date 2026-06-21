class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
            #did this on personal thinking. felt good
        def binary_search(array, target):
            l, r  = 0, len(array)-1
            while l <= r:
                mid = (l + r) // 2
                if array[mid] == target:
                    return mid
                elif array[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return -1
        

        left, right = 0, len(matrix)-1
        
        while left <= right:
            middle = (left + right) // 2
            if max(matrix[middle]) < target:
                left = middle +  1
            elif min(matrix[middle]) > target:
                right = middle - 1
            
            else:
                res = binary_search(matrix[middle], target)
                return res != -1
        
        
        return False







      