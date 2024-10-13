import heapq

class Testing:

    def __init__(self, type):
        self.type = type
        pass


    def maxheap(self, nums):
        if self.type == "heap test":
            # Convert all numbers to negative to simulate max heap
            nums = [-x for x in nums]
            print("Negated nums:", nums)
            
            # Heapify the negated list
            heapq.heapify(nums)
            print("Heapified nums:", nums)
            
            # Extract elements one by one and convert back to positive
            # This is O(N log N) because heappop is Log N and we are ttraversing the entire list which is N. 
            #### way to avoid is this we keep it negative and then convert it back to positive when popped.
            result = [-heapq.heappop(nums) for _ in range(len(nums))]
            print("Final max heap (sorted order):", result)
            
            return result
        else:
            return None

    def minheap(self, nums):
        # O(N)
        heapq.heapify(nums)
        return nums


test = Testing(type="heap test").maxheap([-1,1,2,3,4,5,-6,7,8,9,10])
print("final: ", test)



