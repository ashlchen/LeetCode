
def countDistinct(nums):
    nums = sorted(nums)
    distinct_arr = []
    for i, num in enumerate(nums):
        if i+1 < len(nums):
            if num == nums[i+1]:
                new_num = int(str(num)[::-1])
                if new_num != nums[i+1]:
                    distinct_arr.append(new_num)
                else:
                    continue
            else:
                distinct_arr.append(num)
        
    return len(distinct_arr)


# print(countDistinct([14,15,60,60]))
# print(countDistinct([14,15,60,60]))

def maxNum(num):
    # two pointer
    def helper(start,num):
        maxnum, stop = 0, 0
        for i in range(start, len(num)):
            if int(num[i]) > maxnum:
                maxnum = int(num[i])
                stop = i
        new_num = num[start:stop+1]
        new_num = num[:start]+ new_num[::-1] + num[stop+1:]
        return new_num

    num = str(num)
    maxnum, stop = 0, 0
    for i in range(len(num)):
        if int(num[i]) > maxnum:
            maxnum = int(num[i])
            stop = i
    if stop == 0:
        return helper(1,num)
    new_num = num[:stop+1]
    new_num = new_num[::-1] + num[stop+1:]
    return new_num
    
    
#
print(maxNum(5340))
print(maxNum(1346))
print(maxNum(1000004602))