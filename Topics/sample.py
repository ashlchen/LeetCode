
# now O(n) and space O(1) can be optimized to time O(1) space O(1) by making the input string to list


def maxTime(str):
    # input: string
    # output: string
    res = ""
    for i, num in enumerate(str):
        if i == 0 and num == "?":
            if str[i+1] == "?":
                res += "2"
            elif int(str[i+1]) > 3:
                res += "1"
            else:
                res += "2"
        elif i == 0:
            res += num
        if i == 1 and num == "?":
            if res[0] == "2":
                res += "3"
            else:
                res += "9"
        elif i ==1:
            res += num
        
        if i == 2:
            res += ":"
        if i == 3 and num == "?":
            res += "5"
        elif i == 3:
            res += num
        if i == 4 and num == "?":
            res += "9"
        elif i == 4:
            res += num
    return res

print(maxTime("?4:5?"))
print(maxTime("??:5?"))
print(maxTime("0?:??"))
print(maxTime("??:??"))


def mostBooked(rooms):
    # input a list of sequence of booking
    # output the room that has been booked the most
    
    hmap={}
    for room in rooms:
        if room[0] =="+":
            if room[1:] in hmap:
                hmap[room[1:]] += 1
            else:
                hmap[room[1:]] = 1
    count = 0
    room_num = ""
    for key, value in hmap.items():
        if value > count:
            count = value
            room_num = key
    return room_num

print(mostBooked(["+1A", "+3E", "-1A", "+4F", "+1A", "-3E"]))