import numpy as np

data = open("input_day7.txt" ,'r').read().splitlines()

def is_ok(result, nums):
    if helper(result, nums[0], "+", nums[1:]): return True
    if helper(result, nums[0], "||", nums[1:]): return True
    return helper(result, nums[0], "*", nums[1:])

def helper(result, curr, operator, nums):
    if operator == "||":
        new_result = int(str(curr)+str(nums[0]))
    else:
        new_result = eval(str(curr)+operator+str(nums[0]))
    if new_result > result: return False
    if len(nums) == 1:
        return result == new_result
    if helper(result, new_result, "+", nums[1:]): return True
    if helper(result, new_result, "||", nums[1:]): return True
    return helper(result, new_result, "*", nums[1:])

gold = 0
for row in data:
    s = row.split(":")
    result = int(s[0])
    nums = [int(x) for x in s[1].split()]
    if is_ok(result, nums):
        gold += result
print("Gold:", gold)


