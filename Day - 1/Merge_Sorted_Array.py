nums1 = list(map(int,input().split(' ')))
nums2 = list(map(int,input().split(' ')))
num3 = nums1+nums2
num3 = [n for n in num3 if n != 0]
for i in range(1,len(num3)):
    a = num3[i]
    j = i-1
    while j >= 0 and a < num3[j]:
        num3[j+1] = num3[j]
        j -= 1
        num3[j+1] = a
print(num3)