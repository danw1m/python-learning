# Day6 练习：循环结构
# 对应教程：Python-100-Days\Day01-20\06.循环结构.md
# 老规矩：自己敲，别复制。缩进四个空格，冒号英文。
# 提醒：while 忘了改变量会死循环，卡住了点运行窗口的红色停止按钮。

# ============ 第一块：猜输出（先写答案）============

# 1-1 答案：1 2 3 4(打印出来是竖着的）
# 1-2 答案：1 4 7 （竖着的）
# 1-3 答案：100 50 （竖着的）
# 1-4 答案：10
# 1-5 答案：0 1 2
# 1-6 答案：0 2 4（竖着的）
for i in range(1, 5):
    print(i)

for i in range(1, 10, 3):
    print(i)

for i in range(100, 0, -50):
    print(i)

total = 0
for i in range(1, 5):
    total += i
print(total)

for i in range(10):
    if i == 3:
        break
    print(i)

for i in range(5):
    if i % 2 == 0:
        continue
    print(i)


# ============ 第二块：改错 ============

# 2-1 这段会一直跑不停，为什么？
# i = 1
# while i <= 5:
#     print(i)
# 错在哪：i的值设为1了，但是要停止循环需要i>5,所以会一直打印i
# 改对：
i = 1
while i <= 5:
    i += 1
print(i)

# 2-2
# for i in range(1, 5)
#     print(i)
# 错在哪：少个:
# 改对：
for i in range(1,5):
    print(i)
# 2-3
# for i in range(3):
#     print("开始")
#     break
# 这句会打几次「开始」？为什么？
# 答案：一次，因为后面有break，会让循环停止

# 2-4
# continue
# 单独写在外面会怎样？
# 答案：会报错


# ============ 第三块：写代码（对应本章的例子）============

# 3-1 用 for 算 1 加到 100，打印结果
# 要求：先设 total = 0，循环里累加
my_total = 0
for i in range(1 , 101):
    my_total += i
print(my_total)
# 3-2 用 for 算 1 到 100 里偶数的和
# 提示：range(2, 101, 2) 一个写法就够，不用 if
my_total1 = 0
for i1 in range(2 , 101 , 2):
    my_total1 += i1
print(my_total1)
# 3-3 同样算 1 加到 100，这次用 while 写
# 提示：循环前设 i = 1，循环体里记得让 i 变大
i2 = 1
num = 0
while i2 < 101:
    num += i2
    i2 += 1
print(num)


# 3-4 打印乘法口诀表（对应嵌套循环那个例子）
# 外层控制第几行，内层控制这一行打到第几个
# 提示：print(f'{i}×{j}={i*j}', end='\t')，一行打完用 print() 换行
for q in range(1 , 10):
    for e in range(1 , q+1):
        print(f'{q}*{e}={q*e}', end='\t')
    print()
# 3-5 判断素数（对应例子1）
# 输入一个大于1的正整数，输出是或不是素数
# 提示：从 2 试到它的平方根（int(num ** 0.5)），能整除就 break
n = int(input("请输入一个正整数"))
b = int(n ** 0.5)
is_pro = True
for i in range(2 , b + 1):
    if n % i == 0:
        is_pro = False
        break
if is_pro:
    print(f'{n}是素数')
else:
    print(f'{n}不是素数')


# 3-6 求最大公约数（对应例子2）
# 输入两个正整数，从大到小试，找到第一个能同时整除的就 break
m = int(input("请输入一个数字"))
j = int(input("请再次输入一个"))
for i in range(m , 0 , -1):
    if m % i == 0 and j % i == 0:
        print(f'{i}是最大公因数')
        break
# 3-7 猜数字游戏（对应例子3，今天的重头戏）
# 用 import random 让电脑出 1 到 100 的随机数
# 玩家一直猜，大了提示小一点，小了提示大一点，中了结束
# 最后打印一共猜了几次
# 提示：random.randrange(1, 101)，while True 里放判断，中了就 break
import  random
da = random.randrange(1 , 101)
CS = 0
while True:
    op = int(input("请输入"))
    CS += 1
    if op > da:
        print("大了")
    elif op < da:
        print("小了")
    else:
        print("猜对了")
        break
print(f'你猜了{CS}次')

# ============ 加分题 ============

# 打印 1 到 100 里所有能被 3 整除的数
# 要求：用 continue 跳过不能整除的，不要用 if 包住 print
for i in range(1 , 101):
    if i % 3 != 0:
        continue
    print(i)

# 再想一下：用 for 和 range(3, 101, 3) 也能做到，两行代码就行
# 两种写法都写出来，比较一下哪种更清楚
for i in range(3 , 101 , 3):
    print(i)