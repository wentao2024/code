215	Kth Largest Element in an Array

http://leetcode.com/problems/kth-largest-element-in-an-array/description/



class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        # 1
        nums.sort(reverse = True) 

        #2
        heap = []
        for num in nums:
            heapq.heappush(heap,num)

            if len(heap)>k:
                heapq.heappop(heap)
                    
        return heap[0]
    
        heap

