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