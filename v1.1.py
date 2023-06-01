import random

def spin():
    # 随机生成三个数字
    return [random.randint(1, 9) for i in range(3)]

def check_win(nums):
    # 如果有6则获得特殊奖励
    if 6 in nums:
        print("Congratulations! You win the special prize!")
    else:
        print("Sorry, you didn't win this time.")

def play():
    input("Press Enter to spin the slot machine...")
    nums = spin()
    print(nums)
    check_win(nums)

play()
