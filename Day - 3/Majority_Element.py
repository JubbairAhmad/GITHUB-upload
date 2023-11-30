nums = list(map(int,input().split()))
repeated = {}
for i in nums:
    if i in repeated:
        repeated[i] += 1
    else:
        repeated[i] = 1
maxi = max(repeated, key = repeated.get)
print(maxi)