#Approach : use dict + heap
#Time: O(N log K) => N for dict iteration and log K for heap push and pop
#Space: O(N+k)

from heapq import heappush, heappop
class Solution(object):
    def topKFrequent(self, nums, k):
        hashmap = {}
        heap=[]

        for i in nums:
            hashmap[i] = hashmap.get(i,0)+1


        for num, freq in hashmap.items():

            # push into heap
            heappush(heap, (freq, num))

            # pop when needed
            if len(heap)>k:
                heappop(heap)

        # extract answer from heap
        return [num for freq, num in heap]
