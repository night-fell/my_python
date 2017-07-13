# coding:UTF-8
import math
import cmath
import random

def trans_number(type, x=1.2, y=0):

    u = input(type)
    # 将x转换为整数
    if u == "int":
        return int(x)
    # 将y转换为浮点数
    if u == "float":
        return float(x)
    # 将x转换为复数， 实数部分为x，虚数部分为0
    if u == "complex":
        return complex(x)
    # 将x，y转换为复数， 实数部分为x，虚数部分为y
    if u == "complex1":
        return complex(x, y)

    print(u"常用数学函数")

    # 返回x的绝对值
    if u == "abs":
        return abs(x)
    # 反回最大值
    if u == "max":
        return max(x, y)
    # 返回最小值
    if u == "min":
        return min(x, y)

    # 计算y^2
    if u == "pow":
        return pow(y, 2)

    # 返回平方根
    if u == "sqrt":
        return math.sqrt(y)

def fun(str, a):

    u = input(str)
    s = input(a)
    print(u"常用随机函数")
    #a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

    # 从列表a中随机选中一个
    if u == "choice":
        return random.choice(s)

    # 从指定的范围(2-100按5递增的数据集)中随机选中一个
    if u == "randrange":
        return random.randrange(2, 100, 5)

    # 生成一个随机数，它在(0,1)之间
    if u == "random":
        return random.random()

def fun_tri(type, x):

    u = input(type)
    # 返回x的反余弦弧度值
    if u == "acos":
        return cmath.acos(x)

    # 返回x的正弦弧度值
    if u == "sin":
        return cmath.sin(x)

    # 返回x的余弦弧度值
    if u == "cos":
        return cmath.cos(x)

    if u == "π":
        return cmath.pi
        # 返回π

trans_number1 = trans_number(int)
print (trans_number1)

fun1 = fun(random)
print (fun1)

print ("end")

#fun_tri1 = fun_tri(cos,100)
#print (fun_tri())