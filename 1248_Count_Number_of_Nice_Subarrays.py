'''
Given an array of integers nums and an integer k. 
A continuous subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.
'''
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        codd = 0
        dic = { 0:1 }
        i = 0
        n = len(nums)
        result = 0
        while i < n:
            if nums[i] % 2 == 0:
                dic[codd] += 1
            else:
                codd += 1
                if codd not in dic:
                    dic[codd] = 0
                dic[codd] += 1
            p = codd - k
            if p in dic:
                result += dic[p]
            i += 1
        return result
