import heapq

class Testing:

    def __init__(self):
        pass


    def maxheap(self, nums):
        # O(N)
        nums = [-x for x in nums if x > 0]
        # O(N)
        heapq.heapify(nums)
        # O(N)
        nums = [-x for x in nums if x < 0]
        return nums


    def minheap(self, nums):
        # O(N)
        heapq.heapify(nums)
        return nums


test = Testing().maxheap([1,2,3,4,5,6,7,8,9,10])
print(test)



