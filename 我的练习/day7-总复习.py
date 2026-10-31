# 总复习：Day1 到 Day6（闭卷，不降难度）
# 覆盖：环境、print/input、变量、类型、转换、运算符、分支、循环
#
# ===== 标记规则（重要，做完我会按这个找你的薄弱点）=====
# 1. 闭卷：不翻教程、不翻旧练习、不翻那份 PDF
# 2. 会的，正常写答案
# 3. 拿不准的，答案后面加：# 不确定
# 4. 完全靠猜的，加：# 蒙
# 5. 不会的，留空写：# 不会
# 6. 不许查、不许问我，全做完一起发过来
#
# 时间建议：90 分钟做题，做完别急着对答案，直接叫我

# ============ A 组：快问快答（写在注释里）============

# A1  input() 拿回来的东西是什么类型？
# 答：字符串

# A2  判断两个东西相等，用几个等号？
# 答：两个

# A3  for 和 while，什么时候用哪个？
# 答：知道循环几次用for 不知道时用while

# A4  break 和 continue 的区别？
# 答：break是直接停止循环，continue是跳过这个输出

# A5  range(1, 10, 3) 会产生哪些数？
# 答：1 4 7

# A6  type(3.0) 打出来是什么？
# 答：<'class <float>'>

# A7  变量名 2age 能用吗？为什么？
# 答：不能，数字不能当作变量名的开头

# A8  'abc' 和 "abc" 有区别吗？
# 答：没有


# ============ B 组：猜输出（先写答案，最后统一跑）============

# B1 答案：3 ，1
print(10 // 3, 10 % 3)

# B2 答案：19
print(3 + 4 * 2 ** 2)

# B3 答案：0 1 2 (一排)
for i in range(3):
    print(i, end=" ")

# B4 答案：55 , 10
print("5" + "5", 5 + 5)

# B5 答案：1 3 (竖着的)
for i in range(1, 4):
    if i == 2:
        continue
    print(i)

# B6 答案：15
total = 0
for i in range(1, 6):
    total += i
print(total)

# B7 答案：True , True
print(1 == 1.0, 0 == False)

# B8 答案：A
#         C
x = 5
if x > 3:
    print("A")
else:
    print("B")
print("C")


# ============ C 组：改错（说清错在哪，再写正确的一行）============

# C1
# if x > 3
#     print("大")
# 错在哪：if后面少了：
# 改对：if x > 3:

# C2
# if x = 5:
#     print("等于5")
# 错在哪：比较相等应该用两个==
# 改对：if x == 5:

# C3
# score = 80
# if score >= 90:
# print("A")
# 错在哪：没有缩进
# 改对：
# if score >= 90:
#     print("A")

# C4
# age = "20"
# print(age + 1)
# 错在哪：age是字符串不能直接加整数
# 改对：print(f'{age + 1}')

# C5
# i = 1
# while i <= 5:
#     print(i)
# 错在哪：没有强制停止，会一直循环
# 改对：
# while i <= 5:
#     black
# print(i)
# ============ D 组：写代码（从空白写）============

# D1 输入圆的半径，算面积，保留两位小数
# 提示：面积 = π × r²，用 math.pi#不知道怎么保留两位小数
import math
r = float(input("请输入半径"))
s = math.pi * r ** 2
print("面积：" + f's,2f')
# D2 输入成绩，输出等级：90以上A，80以上B，70以上C，60以上D，其余E
num = int(input("请输入成绩"))
if num >= 90:
    print("A")
elif num >= 80:
    print("B")
elif num >= 70:
    print("C")
elif num >= 60:
    print("D")
else:
    print("E")
# D3 分段函数
# x > 1        y = 3x - 5
# -1 <= x <= 1 y = x + 2
# x < -1       y = 5x + 3
x = int(input("请输入x"))
if x > 1:
    y = 3 * x - 5
    print(y)
elif -1 <= x <= 1:
    y = x + 2
    print(y)
elif x < -1:
    y = 5 * x + 3
    print(y)
# D4 输入一个大于1的整数，判断是不是素数#不太会
num_1 = int(input("请输入一个大于1的整数"))
for i in range(2 , int(num_1 ** 0.5 + 1)):
    if num_1 % i == 0:
        print("是素数")
    else:
        print("不是素数")


# D5 求 1 到 100 里，能同时被 3 和 5 整除的数的和#忘了
# 提示：能被3整除 and 能被5整除
next_x = 0
for i in range(1 , 101):
    if i % 3 == 0 and i % 5 ==0:
        next_x += i
        print(i)
# D6 打印九九乘法表
# 提示：外层 1 到 9，内层到外层为止#忘了


# ============ E 组：综合题 ============

# E1 输入一个三位数，输出它的各位数字之和
# 例：输入 385，输出 16（3+8+5）
# 提示：// 和 % 一起用#强行写的
next_num = int(input("请输入三位数"))
next_num1 = next_num // 100
next_num2 = next_num // 10
next_num3 = next_num2 % 10
next_num4 = next_num % 100
next_num5 = next_num4 % 10
next_max = next_num1 + next_num3 + next_num5
print(next_max)

# E2 猜数字游戏，升级版
# 电脑出 1 到 100 的随机数，玩家最多猜 5 次
# 猜中提示「猜对了」并结束
# 5 次都没中，提示「机会用完了，答案是 xx」
# 提示：用计数器和 while，别写成死循环#循环不会，计数器不知道引用哪个


# ============ 加分题 ============

# F1 求两个正整数的最小公倍数
# 提示：最小公倍数 = 两数相乘 ÷ 最大公约数，最大公约数你昨天写过
x1 = int(input("请输入正整数"))
x2 = int(input("请再次输入"))
