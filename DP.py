class Solution:
    def canJump(self, nums):
        # it really matters if second last num is < than 0
        # than push back to first index to see if there's route to the first index

        # Match
        # look through the list

        # Plan
        # initialize at second to last position
        steps = 0
        # loop backwards until it reach first index
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < steps: # if the current number can't reach the destination
                steps += 1 # move on to the previous number but increase the steps
            else:
                steps = 1  # if can satisfy, move to the previous on and reset to 1
        if nums[0] < steps:
            return False
        return True

    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 and n == 1:
            return 1
        row = [1] * n
        for i in range(m-1):
            newRow = [1] * n
            for j in range(n-2, -1, -1):
                newRow[j] = newRow[j+1] + row[j]
            row = newRow
        return row[0]
    
    def longestPalindrome(self, s):
        # understand
        # "sa": "s" or "a" is a palidrome
        # "1a1" is a palidrome
        # "cbbd": "bb" is a palindrome

        # match
        # DP: try all possible solution, and pick the longest palidrome
        # two pointer

        res = ""
        for i in range(len(s)):
            # odd case
            temp = self.helper(s, i, i)
            if len(temp) > len(res):
                res = temp
            # even case
            temp = self.helper(s, i, i+1)
            if len(temp) > len(res):
                res = temp
        return res
    def helper(self, l, r):
        while l>=0 and r < len(s) and s[l] == s[r]:
            l -=1
            r +=1
        return s[l+1:r]