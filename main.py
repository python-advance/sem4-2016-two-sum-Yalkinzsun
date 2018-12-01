"""
        Two sum from https://leetcode.com/problems/two-sum
"""
class Solution:

    def deco(func):
        import functools
        import time

        @functools.wraps(func)
        def inner(*args, **kwargs):
            start_time = time.time()  # начало таймера
            result = func(*args, **kwargs)
            end_time = time.time()  # завершение таймера
            time_delta = end_time - start_time
            print(f'Время выполнения кода {func.__name__} заняло: {time_delta}')
            return result

        return inner

    @staticmethod
    @deco
    def two_sum_brute(nums, target):  # staticmethod(deco(two_sum_brute))
        """
            :type nums: List[int]
            :type target: int
            :rtype: List[int]
        """

        length = len(nums)
        for i in range(length):
            for j in range(length):
                if nums[j] == target - nums[i]:
                    return [i, j]

    @staticmethod
    @deco
    def two_sum(nums, target):
        """
            :type nums: List[int]
            :type target: int
            :rtype: List[int]
        """
        length = len(nums)
        nums_map = dict()
        for i in range(length):
            nums_map[nums[i]] = i

        for i in range(length):
            diff = target - nums[i]

            if (diff in nums_map.keys()) and (nums_map.get(diff, -1) != i):
                return [i, nums_map.get(diff)]


Solution.two_sum_brute([2, 7, 11, 15], 9)
assert Solution.two_sum_brute([2, 7, 11, 15], 9) == [0, 1], 'проверка случая с единственным сочетанием элементов'
Solution.two_sum([2, 7, 11, 15], 9)
assert Solution.two_sum([2, 7, 11, 15], 9) == [0, 1], 'проверка случая с единственным сочетанием элементов'
