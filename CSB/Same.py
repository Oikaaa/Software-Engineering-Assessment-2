nums1 = [2,3,1,2,4,6]
nums2 = [5,1,3,2,2,4,6,1,8,9,14]

def same_number(nums1, nums2):
    sorted_nums1 = sorted(nums1)
    sorted_nums2 = sorted(nums2)
    output = []
    for x in range(len(sorted_nums1)):
        if sorted_nums1[x] != sorted_nums1[x-1]:
            for y in sorted_nums2:
                if sorted_nums1[x] == y:
                    output.append(sorted_nums1[x])
                    break
    return output
  
output = same_number(nums1, nums2)
print(output)