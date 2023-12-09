with open("day9/day9.txt", "r", encoding="utf-8") as file:
    input = file.readlines()


def one():
    result = 0
    for line in input:
        nums = [int(x) for x in line.split()]
        result += nums[-1]

        while not all(n == 0 for n in nums):
            t_nums = [nums[i + 1] - nums[i] for i in range(len(nums) - 1)]
            result += t_nums[-1]
            nums = t_nums

    print(result)


def two():
    result = 0
    for line in input:
        nums = [int(x) for x in line.split()]
        result += nums[0]
        i = 0

        while not all(n == 0 for n in nums):
            t_nums = [nums[i + 1] - nums[i] for i in range(len(nums) - 1)]

            if i % 2 == 0:
                result -= t_nums[0]
            else:
                result += t_nums[0]
            i += 1

            nums = t_nums

    print(result)


one()
two()
