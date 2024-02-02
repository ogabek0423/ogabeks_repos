class Solution(object):
    @staticmethod
    def twoSum():

        nums = [2, 7, 11, 15]

        target = int(input("target = "))

        for i in range(len(nums)):
            x = target - nums[i]
            if x in nums:
                print(i, nums.index(x))
                break
        return Solution.twoSum()


Solution.twoSum()

