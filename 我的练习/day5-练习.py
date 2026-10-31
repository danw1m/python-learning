# Day5 练习：分支结构
# 对应教程：Python-100-Days\Day01-20\05.分支结构.md
# 老规矩：自己敲，别复制。打印冒号一律英文，缩进一律四个空格。

# ============ 第一块：判断（先把答案写注释里）============

# 1-1 下面这段打出来是什么？
# x = 5
# if x > 3:
#     print("大于3")
# print("结束")
# 答案：大于3
#结束
# 1-2 哪几行属于 if 管？用注释写行号
# if True:
#     print("A")
#     print("B")
# print("C")
# 答案：#16，#17行归if管

# 1-3 猜输出
# score = 75
# if score >= 90:
#     print("A")
# elif score >= 70:
#     print("B")
# else:
#     print("C")
# 答案：B

# 1-4 下面这句会报错吗？为什么？
# if 18.5 <= bmi < 24:
# 答案：不会


# ============ 第二块：改错（说清错在哪，再改正）============

# 2-1
# if x > 3
#     print("大")
# 错在哪：if后面少了:还有可能是x没有赋值
# 改对：if x > 3:

# 2-2
# if x = 5:
#     print("等于5")
# 错在哪：比较应该用双等号
# 改对：if x == 5:

# 2-3
# score = 80
# if score >= 90:
# print("A")
# 错在哪：80不能输出A,应该再加else函数，并且没有缩进4格
# 改对：
score = 80
if score >= 90:
    print("A")
else:
    print("B")
# 2-4
# if x > 0:
#     print("正数")
# else
#     print("不是正数")
# 错在哪：else没有冒号
# 改对：
#if x > 0:
#    print("正数")
#else:
#    print("不是正数")

# ============ 第三块：写代码（对应本章三个例子）============

# 3-1 成绩转等级（对应例子2）
# 90及以上 A，80到90 B，70到80 C，60到70 D，60以下 E
# 提示：从高往低判断，elif 的顺序不能乱
cj = int(input("请输入成绩"))
if cj >= 90:
    print("A")
elif cj >=80:
    print("B")
elif cj >= 70:
    print("C")
elif cj >= 60:
    print("D")
else:
    print("E")
# 3-2 BMI 判断（对应本章开头那个 BMI 计算器）
# 输入身高cm和体重kg，算BMI
# 小于18.5 体重过轻
# 18.5到24 身材很棒
# 24到27 体重过重
# 27以上 肥胖
# 提示：BMI = 体重 / (身高/100) 的平方，判断可以用链式写法 18.5 <= bmi < 24
sg = int(input("请输入身高"))
tz = int(input("请输入体重"))
BIM = tz/( sg / 100) ** 2
if BIM < 18.5:
    print("体重过轻")
elif 18.5 <= BIM < 24:
    print("体重很棒")
elif 24 <= BIM < 27:
    print("体重过重")
else:
    print("肥胖")
# 3-3 分段函数求值（对应例子1）
# x > 1        时  y = 3x - 5
# -1 <= x <= 1 时  y = x + 2
# x < -1       时  y = 5x + 3
# 输入x，输出y
x = float(input("请输入x"))
if x > 1:
    y = 3 * x - 5
elif -1 <= x <= 1:
    y = x + 2
elif x < -1:
    y = 5 * x + 3
print(f'{y = }')
# 3-4 判断奇偶
# 输入一个整数，输出「偶数」或「奇数」
# 提示：用 % 2
zs = int(input("请输入整数"))
if zs % 2 == 0:
    print("偶数")
else:
    print("奇数")
# ============ 第四块：match-case（Python 3.10 新语法）============

# 4-1 用 match-case 写一个「星期几」的判断
# 输入 1 到 7，输出「星期一」到「星期日」
# 输入别的，输出「输入有误」
# 提示：
# match 变量:
#     case 1: print("星期一")
#     case _: print("输入有误")
# case _ 是通配符，放最后
xq = int(input("请输入"))
match xq:
    case 1: print("星期一")
    case 2: print("星期二")
    case 3: print("星期三")
    case 4: print("星期四")
    case 5: print("星期五")
    case 6: print("星期六")
    case 7: print("星期日")
    case _: print("输入有误")
# 4-2 用 match-case 的合并模式改写
# 输入一个 HTTP 状态码：200、301、400、401、403、404、500
# 200 输出 正常
# 301 输出 重定向
# 400 或者 401 或者 403 或者 404 输出 请求有问题
# 500 输出 服务器错误
# 其他输出 未知
# 提示：合并多个值写成 case 400 | 401 | 403 | 404:
ztm = int(input("请输入状态码"))
match ztm:
    case 200: print("正常")
    case 301: print("重定向")
    case 400 | 401 | 403 | 404: print("请求有问题")
    case 500: print("服务器错误")
    case _: print("未知")
# ============ 第五块：综合 ============

# 判断能不能构成三角形（对应例子3）
# 输入三条边，如果两边之和都大于第三边，输出周长和面积，否则输出「不能构成三角形」
# 面积用海伦公式：s = 周长/2，面积 = (s*(s-a)*(s-b)*(s-c)) 的 0.5 次方
# 提示：** 0.5 就是开平方
ab = float(input("请输入a边"))
bb = float(input("请输入b边"))
cb = float(input("请输入c边"))
if ab + bb > cb and bb + cb > ab and ab + cb > bb:
    zc = ab + bb + cb
    s = (ab + bb + cb) / 2
    mj = (s * (s - ab) * (s - bb) * (s - cb)) ** 0.5
    print("周长:" + str(zc))
    print("面积:" + str(mj))
else:
    print("不能构成三角形")
# ============ 加分题 ============

# 猜数字第一版（还没学循环，只能猜一次）
# 程序里先定一个数 answer = 42
# 输入你猜的数
# 大了输出「大了」，小了输出「小了」，中了输出「猜对了」
answer = int(input("请输入数字"))
if answer < 42:
    print("小了")
elif answer == 42:
    print("猜对了")
elif answer > 42:
    print("大了")