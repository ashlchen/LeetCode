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