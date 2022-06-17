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


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        # Understand
        # m,n >=1 ... the matrix exists
        # not necessary square matrix
        # m = row
        # n = column
        
        # Match
        # two pointers: set boundaries, manipulate the progress accordingly

        # Plan
        # get l, r boundary and top, bottom boundary
        l, r = 0, len(matrix[0]) - 1
        t, b = 0, len(matrix) - 1
        # output array
        res = []
        while r>=l and b>=t:
            for i in range(l, r+1):
                cur = matrix[t][i]
                res.append(cur)
        # re-initiatei pointers: top row has been done
            t += 1
    # when l == r, then start going vertically
            for i in range(t, b+1):
                cur = matrix[i][r]
                res.append(cur)
        # re-initiate pointers: the right most column has been seen
            r -= 1
    # when t == b, then start going horozontally
            if t <= b:
                for i in range(r, l-1, -1):
                    cur = matrix[b][i]
                    res.append(cur)
        # re-initaite pointers: the bottom has been seen
                b -= 1
    # when r == l, go vertically, but - 1
            if l <= r:
                for i in range(b, t-1, -1):
                    cur = matrix[i][l]
                    res.append(cur)
        # re-initiate pointers
                l += 1
        return res

# test case
m1 = [[0]]        # zero
m2 = [[-1]]       # negative  
m3 = [[2,2],[2,2]] # duplicate