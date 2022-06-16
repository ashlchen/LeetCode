def rotate(self, matrix: List[List[int]]):
        """
        Do not return anything, modify matrix in-place instead.
        """
    # understand
        # rotate the image in place
        # it's a n*n matrix
        # it exists (1<=n<=20)
        # the value of each cell might have negative number

    # match
        # 2 pointer
    # plan
        # initiatie pointers at leftmost and rightmost
        # store the left pointer into a variable "temp"
        # start circular rotation
        # go to next square
        # stop the outer layer when first row has been visited (left = right)
        # go to next layer (left = 1, right = len - 2)
        # stop when no more cell can be rotated (l = r)
        # don't return anything

    l, r = 0, len(matrix[0]) - 1
    row, col = 0, 0
    while l < r:
        for i in r:
            temp = matrix[row][col]
            # move bottom left to upper left
            matrix[row][col] = matrix[r-i][col-i]
            # move bottom right to bottom left
            matrix[r-i][col-i] = matrix[r][r-i]
            # move upper right to buttom right
            matrix[r][r-i] = matrix[row+i][r]
            # move upper left to upper right
            matrix[row+i][r] = temp
            col += 1
        row += 1
        col = row
        l += 1
        r -= 1
# test case
m1 = [[0]]
m2 = [[0,1],[1,-1]]
m3 = [[2,2],[2,2]]
m4 = [[1,2,3],[4,5,6],[7,8,9]]