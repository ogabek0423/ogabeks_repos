class Solution(object):
    @staticmethod
    def twoSum():

        nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

        target = int(input("target = "))

        for i in range(len(nums)):
            x = target - nums[i]
            if x in nums:
                print(i, nums.index(x))
                break
        return Solution.twoSum()


Solution.twoSum()

