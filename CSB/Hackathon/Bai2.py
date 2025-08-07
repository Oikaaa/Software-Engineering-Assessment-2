import math

nums = [3, 2, 3]
nums2 = [1]
nums3 = [1, 2]

def Appear_more_than_avr(list):
    output = []
    n = len(list) 
    avr = math.floor(n/3)
    current_num = 10**10
    for i in sorted(list):
        if current_num != i: 
            time_appear = list.count(i) 
            if time_appear > avr: 
                output.append(i)
        current_num = i
    return output

print(Appear_more_than_avr(nums))
print(Appear_more_than_avr(nums2))
print(Appear_more_than_avr(nums3))