#!/usr/bin/env python3
 
def pandigital(nums):
    lst= []
    if type(nums) == int:
        nums = (nums,)
    for num in nums:
        num = str(num)
        for i in range(1, len(num) + 1):
            if num.count(str(i)) != 1:
                break
        else:
            lst.append(int(num))
            print(num)
    if not lst:
        print("not found")
    return lst

if __name__ == "__main__":
    lst = pandigital(eval(input()))
