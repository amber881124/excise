# 寫一個function來印出誰的成績是第二高，如果超過一個人分數都是第二高，請把人名一行一行印出來。
# students：一個二維清單，例如 [['Jerry', 88], ['Justin', 84], ['Tom', 90], ['Akriti', 92], ['Harsh', 90]] 
# 不須回傳

# 期望的執行結果：
# students = [['Jerry', 88], ['Justin', 84], ['Tom', 90], ['Akriti', 92], ['Harsh', 90]]  
# second_highest(students)印出：
# Tom
# Harsh

# 重要提示：
# 不一定要，但可以使用sorted這個function來排列清單，
# x = [3, 1, 4, 5, 2]
# x = sorted(x) # 排列x (由小到大)
# print(x) # 印出 [1, 2, 3, 4, 5]
# 如果要顛倒排列也可以，只要多加reverse=True
# x = [3, 1, 4, 5, 2]
# x = sorted(x, reverse=True) # 排列x (由大到小)
# print(x) # 印出 [5, 4, 3, 2, 1]


students = [['Jerry', 100], ['Justin', 84], ['Tom', 90], ['Akriti', 92], ['Harsh', 100]]  


def second_highest(students):
    new = []
    for name, score in students:
        new.append([score, name])
    new = sorted(new, reverse = True)
    for score, name in new:
        if score == new[1][0]:
            print(name)

second_highest(students)    