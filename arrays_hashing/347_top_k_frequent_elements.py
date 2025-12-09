#Appraoch: use dict() to store frequency and sort based on dictionary keys using sorted() and lambda function()
#Time: O(N log N) -> Due to for loop + sorting
#Space:O(N) -> due to dict and sorted new list
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = dict()

        for i in nums:
            hashmap[i] = hashmap.get(i, 0) + 1

        sorted_list = sorted(hashmap.items(), key = lambda x: x[1], reverse = True)        

        return [i[0] for i in sorted_list[:k]]