class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        def ls(arr, num):
            for i in range(len(arr)):
                if arr[i] == num:
                    return True
            return False

        longest = 0

        for i in range(len(nums)):
            n = nums[i]
            count = 1

            while ls(nums, n + 1):
                n += 1
                count += 1

            longest = max(longest, count)

        return longest