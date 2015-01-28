nums = 1:999
res = sum(nums[!(nums %% 3) | !(nums %% 5)])
print(res)

