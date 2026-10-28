nums = [10, 20, 30, 20, 40, 10, 50]
fc = {}
for i in range(len(nums)):
    if fc.get(nums[i]) is None:
        fc[nums[i]] = 1
    else:
        fc[nums[i]] += 1
print(fc)